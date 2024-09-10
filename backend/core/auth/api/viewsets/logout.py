from rest_framework_simplejwt.tokens import TokenError
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class LogoutViewSet(viewsets.ViewSet):
    """
        ViewSet for handling user logout requests.

        This ViewSet provides a `create` method for handling logout requests
        by invalidating the provided refresh token.
    """
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        """
            Handles POST requests to log out users by invalidating the refresh token.

            The refresh token should be provided in the request data. If the token is valid,
            it will be added to the blacklist to prevent future use.

            Args:
                request (Request): The incoming request containing the refresh token.

            Returns:
                Response: A Response object with a 204 No Content status if the logout was successful,
                          or a 400 Bad Request status if the token is invalid or missing.
        """
        refresh = request.data.get("refresh")
        if refresh is None:
            raise ValidationError({"detail": "A refresh token is required."})

        try:
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            raise ValidationError({"detail": "The refresh token is invalid."})
