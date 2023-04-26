"""
Product Attribute Values
"""
from django.db import models

from .product_attribute_value import ProductAttributeValue
from .product_inventory import ProductInventory


class ProductAttributeValues(models.Model):
    """
    Product Attribute Values
    """

    attribute_values = models.ForeignKey(
        ProductAttributeValue,
        related_name="product_attr_values",
        on_delete=models.PROTECT,
    )
    product_inventory = models.ForeignKey(
        ProductInventory, related_name="product_attr_values", on_delete=models.PROTECT
    )

    class Meta:
        """
        Meta information
        """

        unique_together = (("attribute_values", "product_inventory"),)
