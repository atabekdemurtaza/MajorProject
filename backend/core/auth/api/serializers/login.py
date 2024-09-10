from typing import Any, Dict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from core.user.api.serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    """
        Custom serializer to handle token authentication with additional user details.
    """

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        """
           Validate the provided credentials and return the JWT tokens along with user data.

           Args:
               attrs (Dict[str, Any]): Contains 'email' and 'password'.

           Returns:
               Dict[str, str]: Contains 'refresh', 'access', and 'user' data.

           Raises:
               serializers.ValidationError: If authentication fails.
        """
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
