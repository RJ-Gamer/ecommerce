"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import ProductAttribute


class ProductAttributeSerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        model = ProductAttribute
        fields = "__all__"
