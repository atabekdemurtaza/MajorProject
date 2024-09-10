from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    """
    Serializer for the User model. Inherits from AbstractSerializer to include
    common fields like id, created, and updated.
    """

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'created', 'updated'
        ]
        read_only_fields = ['is_active']  # is_active is read-only to prevent changes via this serializer
