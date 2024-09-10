from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from typing import Dict, Any


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer to handle token authentication with email as the username field.

    This serializer allows for authentication using an email address instead of a username.

    Attributes:
    - `username_field`: Specifies that the 'email' field should be used for authentication.

    Methods:
    - `validate`: Validates the provided credentials and returns JWT tokens.
    """
    username_field = 'email'

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        """
        Validate the provided credentials and return the JWT tokens.

        Args:
            attrs (Dict[str, Any]): Contains 'email' and 'password'.

        Returns:
            Dict[str, str]: Contains 'refresh' and 'access' tokens.

        Raises:
            serializers.ValidationError: If email or password is not provided, or if authentication fails.
        """
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)

            if not user:
                raise serializers.ValidationError('No active account found with the given credentials')

            refresh = self.get_token(user)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }

            return data
        else:
            raise serializers.ValidationError('Must include "email" and "password"')
