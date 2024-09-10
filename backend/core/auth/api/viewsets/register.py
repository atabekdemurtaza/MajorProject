from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.api.serializers import RegisterSerializer


class RegisterViewSet(ViewSet):
    """
        ViewSet for handling user registration.

        Allows public access for creating new user accounts and issuing JWT tokens.
    """
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """
            Handle POST requests to register a new user.

            Validates the provided data, creates a new user, and issues JWT tokens.

            Args:
                request (Request): The incoming request containing user registration data.

            Returns:
                Response: A Response object containing the newly created user's data,
                          along with JWT refresh and access tokens.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "user": serializer.data,
                "refresh": res["refresh"],
                "token": res["access"],
            }, status=status.HTTP_201_CREATED
        )

    def http_method_not_allowed(self, request, *args, **kwargs):
        """
            Handles requests with methods not allowed for this view.

            Args:
                request (Request): The incoming request with an unsupported method.

            Returns:
                Response: A Response object with a 405 Method Not Allowed status
                          and a message indicating the allowed methods.
        """
        allowed_methods = ', '.join(self.http_method_names)
        return Response(
            {
                "detail": f"Only {allowed_methods} method(s) are/is allowed."
            },
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
