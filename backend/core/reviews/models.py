from django.db import models
from django.core.exceptions import ValidationError
from core.abstract.models import AbstractModel, AbstractManager


def validate_rating(value):
    """
    Validator to ensure that the rating is between 1 and 5.

    Args:
        value (int): The rating value to validate.

    Raises:
        ValidationError: If the rating is not between 1 and 5.
    """
    if value < 1 or value > 5:
        raise ValidationError('Rating must be between 1 and 5')


class ReviewManager(AbstractManager):
    """
    Custom manager for the Review model.
    """
    pass


class Review(AbstractModel):
    """
    Represents a review for a product.

    Attributes:
        product (ForeignKey): The product being reviewed.
        author (ForeignKey): The user who wrote the review.
        rating (IntegerField): The rating given to the product (1-5).
        comment (TextField): The text of the review.
        edited (BooleanField): Flag indicating if the review has been edited.
    """
    product = models.ForeignKey('core_product.Product', on_delete=models.PROTECT, related_name='reviews')
    author = models.ForeignKey('core_user.User', on_delete=models.PROTECT, related_name='reviews')
    rating = models.IntegerField(default=0, validators=[validate_rating], help_text="Rating from 1 to 5")
    comment = models.TextField(help_text="The review text")
    edited = models.BooleanField(default=False, help_text="Indicates if the review has been edited")

    objects = ReviewManager()

    def __str__(self):
        return f'Review by {self.author.name} on {self.product.name}'

    class Meta:
        db_table = 'core_reviews'
        unique_together = ('author', 'product')  # Prevents multiple reviews by the same user for the same product
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created']  # Orders reviews by creation date, newest first
