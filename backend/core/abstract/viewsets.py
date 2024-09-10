from rest_framework import viewsets
from rest_framework import filters
from typing import List, Type


class AbstractViewSet(viewsets.ModelViewSet):
    """
    An abstract base viewset for models using UUIDs for primary keys and timestamp fields.

    This viewset provides common configurations for filtering and ordering of queryset.

    Attributes:
    - `filter_backends` (List[Type[filters.BaseFilterBackend]]): List of filter backends used for filtering the queryset.
    - `ordering_fields` (List[str]): List of fields that can be used for ordering the queryset.
    - `ordering` (List[str]): Default ordering applied to the queryset.
    """

    filter_backends: List[Type[filters.BaseFilterBackend]] = [filters.OrderingFilter]
    ordering_fields: List[str] = ['updated', 'created']
    ordering: List[str] = ['-updated']
