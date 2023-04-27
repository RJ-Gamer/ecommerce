"""
Product Inventory Views
"""
from rest_framework import status, viewsets, pagination
from rest_framework.response import Response

from ecommerce.inventory.serializers import ProductInventorySerializer
from ecommerce.inventory.models import ProductInventory
from shared.utils import messages


class GetProductInventoryListViewSet(viewsets.ModelViewSet):
    """
    Get list of Product Inventory
    """

    serializer_class = ProductInventorySerializer
    http_method_names = ["get"]
    lookup_field = "sku"
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        """
        Get queryset
        """
        return ProductInventory.objects.filter(is_active=True).order_by("id")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)
