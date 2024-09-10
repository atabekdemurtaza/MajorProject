from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from core.product.models import Product
from core.product.api.serializers import ProductSerializer
from core.abstract.viewsets import AbstractViewSet


class ProductViewSet(AbstractViewSet):
    """
        ViewSet for handling operations on Product model.
        - GET: List all products or filter by authenticated user.
        - POST: Create a new product (authenticated users only).
        - PUT/PATCH: Update an existing product (authenticated users only).
        - DELETE: Delete an existing product (authenticated users only).
    """
    http_method_names = ('post', 'get', 'put', 'delete')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        """
            Return the permission classes based on the request method.
        """
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)
        elif self.request.method == 'POST':
            self.permission_classes = (IsAuthenticated,)
        return super(ProductViewSet, self).get_permissions()

    def get_queryset(self):
        """
            Return a queryset of products.
            Authenticated users see their own products; unauthenticated users see all products.
        """
        if self.request.user.is_authenticated:
            return Product.objects.filter(author=self.request.user)
        return Product.objects.all()

    def get_object(self):
        """
            Retrieve an object based on the public_id.
        """
        obj = Product.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        """
            Create a new product.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update an existing product.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an existing product.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
