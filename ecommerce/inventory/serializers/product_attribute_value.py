"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import ProductAttributeValue

from .product_attribute import ProductAttributeSerializer


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        product_attribute = ProductAttributeSerializer()

        model = ProductAttributeValue
        fields = "__all__"
