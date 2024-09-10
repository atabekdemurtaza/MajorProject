from rest_framework import serializers
from core.user.api.serializers import UserSerializer
from core.user.models import User


class RegisterSerializer(UserSerializer):
    """
    Registration serializer for handling user registration requests.

    This serializer extends `UserSerializer` to include the password field
    and handle user creation.

    Attributes:
        password (CharField): The password field for user registration.
    """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        required=True
    )
    """
    Password field for user registration.
    - `max_length`: Maximum length of the password (128 characters).
    - `min_length`: Minimum length of the password (8 characters).
    - `write_only`: Ensures the password is not exposed in responses.
    - `required`: Indicates that this field is mandatory for registration.
    """

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]
    """
    Meta class to specify the model and fields used by this serializer.
    - `model`: Specifies the User model for serialization.
    - `fields`: List of fields to include in serialization.
    """

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.

        Args:
            validated_data (dict): Data validated by the serializer, including the password.

        Returns:
            User: The created user instance.
        """
        return User.objects.create_user(**validated_data)
