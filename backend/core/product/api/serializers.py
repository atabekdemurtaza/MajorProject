from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.product.models import Product
from core.user.api.serializers import UserSerializer
from core.user.models import User


class ProductSerializer(AbstractSerializer):
    """
        Serializer for the Product model.

        Handles serialization and deserialization of Product data.
        - `author`: User who created the product.
        - `name`: Name of the product.
        - `description`: Description of the product.
        - `price`: Price of the product.
        - `edited`: Indicates if the product has been edited.
        - `created`: Timestamp when the product was created.
        - `updated`: Timestamp when the product was last updated.
    """
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id'
    )

    def validate_author(self, value):
        """
            Validate that the user creating the product is the same as the author.

            Args:
                value: The author of the product being created.

            Raises:
                ValidationError: If the request user does not match the author.

            Returns:
                 value: The validated author.
        """
        if self.context["request"].user != value:
            raise ValidationError("You cannot create a post for another user.")
        return value

    def to_representation(self, instance):
        """
            Convert the Product instance to a JSON-serializable format.

            Args:
                - instance: The Product instance being serialized.

            Returns:
                - rep: The serialized representation of the product, including the author as a nested representation.
        """
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        return rep

    def update(self, instance, validated_data):
        """
            Update an existing Product instance with the provided data.

            Args:
                - instance: The Product instance to update.
                - validated_data: The data to update the instance with.

            Returns:
                - instance: The updated Product instance.
        """
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'author', 'edited', 'created', 'updated'
        ]
        read_only_fields = ['edited']
