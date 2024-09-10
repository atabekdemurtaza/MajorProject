import pytest

from core.product.models import Product
from core.fixtures.user import test_user

user = test_user


@pytest.mark.django_db
def test_product_creation(user):
    product = Product.objects.create(
        author=user,
        name='Test Product',
        description='Test Description',
        price=10,
    )
    assert product.name == 'Test Product'
    assert product.author == user
    assert product.description == 'Test Description'
    assert product.price == 10
