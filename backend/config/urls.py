from django.contrib import admin
from django.urls import path, include
from core.ml_models.views import ProductRecommendationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(("core.routers", "core"), namespace="core-api")),
    path('recommendations/<int:product_id>/', ProductRecommendationView.as_view(), name='product-recommendation'),
]
