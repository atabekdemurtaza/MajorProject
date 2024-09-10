import pytest
from core.user.models import User
from core.user.tests.test_user import data_user


@pytest.fixture
def test_user(db) -> User:
    return User.objects.create_user(**data_user)
