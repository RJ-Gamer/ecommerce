"""
Product Type Attributes
"""
from django.db import models

from .product_attribute import ProductAttribute
from .product_type import ProductType


class ProductTypeAttribute(models.Model):
    """
    Product Type Attributes
    """

    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attrs",
        on_delete=models.PROTECT,
    )
    product_type = models.ForeignKey(
        ProductType, related_name="product_type_attrs", on_delete=models.PROTECT
    )

    class Meta:
        """
        Meta information
        """

        unique_together = (("product_attribute", "product_type"),)
