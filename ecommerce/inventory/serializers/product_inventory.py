"""
Product Inventory Serializer
"""
from rest_framework import serializers
from ecommerce.inventory.models import ProductInventory

from .brand import BrandSerializer
from .product import ProductSerializer
from .tag import TagSerializer
from .product_type import ProductTypeSerializer
from .product_attribute_value import ProductAttributeValueSerializer


class ProductInventorySerializer(serializers.ModelSerializer):
    """
    Product Inventory Serializer
    """

    tags = TagSerializer(many=True)
    product_type = ProductTypeSerializer()
    product = ProductSerializer()
    brand = BrandSerializer()
    attribute_values = ProductAttributeValueSerializer(many=True)

    class Meta:
        """
        Meta information for Product Inventory Serializer
        """

        model = ProductInventory
        fields = "__all__"
