"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import ProductType


class ProductTypeSerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        model = ProductType
        fields = "__all__"
