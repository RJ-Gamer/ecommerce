"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        model = Tag
        fields = "__all__"
