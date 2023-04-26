"""
Product Attribute Value Model
"""
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .product_attribute import ProductAttribute


class ProductAttributeValue(models.Model):
    """
    Product Attribute Model
    """

    product_attribute = models.ForeignKey(
        ProductAttribute, related_name="attribute_values", on_delete=models.PROTECT
    )
    value = models.TextField(_("Value"), null=True, blank=True)

    class Meta:
        """
        Meta information for Product objects
        """

        verbose_name = _("Product Attribute Value")
        verbose_name_plural = _("Product Attribute Values")

    def __str__(self):
        """
        String representation of Product object
        """
        return f"{self.value}"
