from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from core.user.api.viewsets import UserViewSet
from core.auth.api.viewsets.register import RegisterViewSet
from core.auth.api.viewsets.login import LoginViewSet
from core.auth.api.viewsets.refresh import RefreshViewSet
from core.auth.api.viewsets.logout import LogoutViewSet

from core.product.api.viewsets import ProductViewSet
from core.reviews.api.viewsets import ReviewViewSet


router = routers.SimpleRouter()

# User
router.register(r'users', UserViewSet, basename='user')

# Auth
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'auth/logout', LogoutViewSet, basename='auth-logout')

# Product
router.register(r'products', ProductViewSet, basename='products')

# Review
product_router = nested_routers.NestedDefaultRouter(router, r'products', lookup='products')
product_router.register(r'reviews', ReviewViewSet, basename='product-reviews')


urlpatterns = [
    *router.urls,
    *product_router.urls,
]
