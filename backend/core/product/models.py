from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


class ProductManager(AbstractManager):
    """
    Custom manager for the Product model.

    This manager provides additional methods for querying Product instances if needed.
    """
    pass


class Product(AbstractModel):
    """
    Represents a product in the system.

    Attributes:
        author (ForeignKey): Reference to the user who created the product.
        name (CharField): The name of the product.
        description (TextField): A detailed description of the product.
        price (DecimalField): The price of the product.
        edited (BooleanField): Flag indicating if the product has been edited.
    """
    author = models.ForeignKey(
        'core_user.User',
        on_delete=models.CASCADE,
        related_name='products',
        help_text="The user who created the product."
    )
    name = models.CharField(
        max_length=255,
        help_text="Name of the product"
    )
    description = models.TextField(
        help_text="Detailed description of the product"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price of the product"
    )
    edited = models.BooleanField(
        default=False,
        help_text="Indicates whether the product has been edited"
    )

    objects = ProductManager()

    def __str__(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: A string describing the product with its name and author.
        """
        return f'Product: {self.name} by {self.author.name}'

    class Meta:
        db_table = "core_product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created']  # Orders products by creation date, newest first
