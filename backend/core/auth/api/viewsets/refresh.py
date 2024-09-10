from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView


class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    """
        ViewSet for handling token refresh requests.

        Inherits from TokenRefreshView to provide token refresh functionality
        while allowing public access.
    """
    permission_classes = (AllowAny, )
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """
            Handles POST requests to refresh tokens.

            Expects a request containing a refresh token. If valid, a new access token
            will be issued. If the refresh token is invalid, an error will be returned.

            Args:
                request (Request): The incoming request containing the refresh token.

            Returns:
                Response: A Response object with the new access token and refresh token
                          or an error message if the token is invalid.
        """
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

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
