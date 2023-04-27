"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        model = Brand
        fields = ["title", "image", "category"]
