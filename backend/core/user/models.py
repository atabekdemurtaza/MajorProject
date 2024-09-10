import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


class UserManager(BaseUserManager, AbstractManager):
    """
    Custom manager for the User model, providing methods for creating users and superusers.
    """
    def get_object_by_public_id(self, public_id: uuid.UUID):
        """
        Retrieves a User instance by its public_id.

        Args:
            public_id (uuid.UUID): The public identifier of the user.

        Returns:
            User: The user instance if found.

        Raises:
            ObjectDoesNotExist: If the user with the given public_id does not exist.
        """
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise ObjectDoesNotExist("User not found.")

    def create_user(self, username: str, email: str, password: str = None, **kwargs):
        """
        Creates and returns a regular user with the given username, email, and password.

        Args:
            username (str): The username for the user.
            email (str): The email address for the user.
            password (str): The password for the user.

        Returns:
            User: The created user instance.

        Raises:
            ValueError: If username, email, or password is not provided.
        """
        if username is None:
            raise ValueError('Users must have a username.')
        if email is None:
            raise ValueError('Users must have an email.')
        if password is None:
            raise ValueError('Users must have a password.')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username: str, email: str, password: str = None, **kwargs):
        """
        Creates and returns a superuser with the given username, email, and password.

        Args:
            username (str): The username for the superuser.
            email (str): The email address for the superuser.
            password (str): The password for the superuser.

        Returns:
            User: The created superuser instance.
        """
        user = self.create_user(username=username, email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    """
    Custom User model with UUID as the primary key and additional fields for authentication and authorization.

    Attributes:
        public_id (UUIDField): Unique identifier for the user.
        username (CharField): Username for the user.
        first_name (CharField): User's first name.
        last_name (CharField): User's last name.
        email (EmailField): User's email address.
        is_active (BooleanField): Indicates whether the user is active.
        is_staff (BooleanField): Indicates whether the user has staff privileges.
        is_superuser (BooleanField): Indicates whether the user has superuser privileges.
        created (DateTimeField): Timestamp when the user was created.
        updated (DateTimeField): Timestamp when the user was last updated.
    """
    public_id = models.UUIDField(
        db_index=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        db_index=True,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self) -> str:
        """
        Returns a string representation of the user instance.

        Returns:
            str: The username of the user.
        """
        return f'{self.username}'

    @property
    def name(self) -> str:
        """
        Returns the full name of the user.

        Returns:
            str: The full name of the user in the format 'first_name - last_name'.
        """
        return f'{self.first_name} - {self.last_name}'
