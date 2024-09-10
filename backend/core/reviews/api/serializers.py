from rest_framework import serializers
from core.reviews.models import Review
from core.user.models import User
from core.product.models import Product
from core.product.api.serializers import ProductSerializer
from core.user.api.serializers import UserSerializer
from core.abstract.serializers import AbstractSerializer


class ReviewSerializer(AbstractSerializer):
    """
    Serializer for the Review model. This serializer includes the details
    of the review, including the product and author details, with validation
    to ensure the correct user is creating the review.
    """
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id',
    )
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field='public_id',
    )

    def validate_author(self, value):
        """
        Validate that the user creating the review is the same as the author.
        """
        if self.context['request'].user != value:
            raise serializers.ValidationError("You cannot create a review for another user.")
        return value

    def to_representation(self, instance):
        """
        Return a representation of the review with detailed product and author information.
        """
        rep = super().to_representation(instance)
        rep['author'] = UserSerializer(instance.author).data
        rep['product'] = ProductSerializer(instance.product).data
        return rep

    class Meta:
        model = Review
        fields = [
            'id', 'product', 'author', 'rating', 'comment', 'edited', 'created', 'updated'
        ]
        read_only_fields = ['edited']
