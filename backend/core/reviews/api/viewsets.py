from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.reviews.models import Review
from core.reviews.api.serializers import ReviewSerializer
from core.abstract.viewsets import AbstractViewSet


class ReviewViewSet(AbstractViewSet):
    """
    A viewset for viewing and editing Review instances.
    - GET: List all reviews or retrieve a specific review.
    - POST: Create a new review.
    - PUT: Update an existing review.
    - DELETE: Delete a review.
    """
    http_method_names = ('get', 'post', 'put', 'delete')
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        """
        Returns different permissions based on the request method.
        """
        if self.request.method in ['GET']:
            self.permission_classes = (AllowAny,)
        elif self.request.method in ['POST', 'PUT', 'DELETE']:
            self.permission_classes = (IsAuthenticated,)
        return super(ReviewViewSet, self).get_permissions()

    def get_queryset(self):
        """
        Returns a queryset of reviews. Filters by the logged-in user for authenticated users.
        """
        if self.request.user.is_authenticated:
            return Review.objects.filter(author=self.request.user)
        return Review.objects.all()

    def get_object(self):
        """
        Returns the review instance based on the provided public_id.
        """
        obj = Review.objects.get_object_by_public_id(self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        """
        Creates a new review instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Updates an existing review instance.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes a review instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
