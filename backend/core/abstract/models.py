from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from typing import Type


class AbstractManager(models.Manager):
    """
        Custom manager for AbstractModel to handle common queries.
    """

    def get_object_by_public_id(self, public_id: uuid.UUID) -> Type[models.Model]:
        """
            Retrieves an instance by its public_id.

            Args:
                public_id (UUID): The public identifier of the object.

            Returns:
                instance: The object instance if found.

            Raises:
                Http404: If the object with the given public_id does not exist.
        """
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise Http404("Object not found")


class AbstractModel(models.Model):
    """
        Abstract base model with common fields for other models.
    """
    public_id = models.UUIDField(
        db_index=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract = True
