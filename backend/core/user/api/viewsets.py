from rest_framework.permissions import IsAuthenticated
from core.user.models import User
from core.user.api.serializers import UserSerializer
from core.abstract.viewsets import AbstractViewSet


class UserViewSet(AbstractViewSet):
    """
    ViewSet for handling operations related to the User model.
    Allows authenticated users to view and partially update user information.
    """
    http_method_names = ('get', 'patch')  # Allow GET and PATCH requests
    permission_classes = (IsAuthenticated,)  # Only authenticated users can access
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Returns a queryset of users. For authenticated users, returns all users.
        For unauthenticated requests, excludes superusers.
        """
        if self.request.user.is_authenticated:
            return User.objects.all()  # Return all users if authenticated
        return User.objects.exclude(is_superuser=True)  # Exclude superusers if not authenticated

    def get_object(self):
        """
        Retrieves a user object by its public_id from the URL.
        Checks permissions to ensure the user can access the object.
        """
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)  # Ensure permissions are checked
        return obj
