import random
from django.core.management.base import BaseCommand
from core.user.models import User
from core.product.models import Product
from core.reviews.models import Review
from decimal import Decimal
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with test data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker()  # Create a Faker instance

    def handle(self, *args, **kwargs):
        # Create users
        users = []
        for _ in range(50):
            user = User.objects.create_user(
                username=self.faker.user_name(),
                email=self.faker.email(),
                password='12345678',
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
            )
            users.append(user)

        # Create products
        products = []
        for _ in range(50):
            product = Product.objects.create(
                author=random.choice(users),
                name=self.faker.name() + " " + self.faker.word(),
                description=self.faker.text(),
                price=Decimal(self.faker.pydecimal(left_digits=2, right_digits=2, positive=True)),
            )
            products.append(product)

        # Create reviews
        for _ in range(50):
            Review.objects.create(
                product=random.choice(products),
                author=random.choice(users),
                rating=random.randint(1, 5),
                comment=self.faker.text(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
