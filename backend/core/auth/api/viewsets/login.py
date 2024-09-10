from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from core.auth.api.serializers import LoginSerializer


class LoginViewSet(ViewSet):
    """
        ViewSet for handling user login requests.

        This ViewSet provides a `create` method for user login and token generation.
        It uses `LoginSerializer` to validate credentials and `CustomTokenObtainPairSerializer`
        to generate and return access and refresh tokens.
    """
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """
            Handles POST requests for user login.

            This method accepts `email` and `password` in the request data,
            validates the credentials using the `LoginSerializer`, and
            returns the access and refresh tokens if the credentials are valid.

            Args:
                request (Request): The incoming request containing `email` and `password`.

            Returns:
                Response: A Response object containing the access and refresh tokens, or
                          an error message if the credentials are invalid.
        """
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
