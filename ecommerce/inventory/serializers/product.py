"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        model = Product
        fields = ["title", "category"]
