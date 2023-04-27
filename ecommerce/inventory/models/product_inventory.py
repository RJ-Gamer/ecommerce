"""
Product Inventory Model
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from shared.utils.functions import generate_unique_code
from shared.utils import constants

from .tag import Tag
from .product_type import ProductType
from .product import Product
from .brand import Brand
from .product_attribute_value import ProductAttributeValue
from .abstract import AbstractTimeStamp


class ProductInventory(AbstractTimeStamp, models.Model):
    """
    Product Inventory Model
    """

    uid = models.CharField(
        _("Product Inventory UID"),
        max_length=16,
        unique=True,
        db_index=True,
        editable=False,
        default=generate_unique_code(length=constants.PRODUCT_UID_LEN),
    )
    sku = models.CharField(_("Stock Keeping Unit"), max_length=25, unique=True)
    upc = models.CharField(_("UPC"), max_length=25, unique=True)
    product_type = models.ForeignKey(
        ProductType, related_name="product_inventories", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name="product_inventories", on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand,
        related_name="brand_inventories",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_attribute_values",
        through="ProductAttributeValues",
    )
    is_default = models.BooleanField(_("Is Default"), default=False)
    is_digital = models.BooleanField(_("Is Digital"), default=False)
    is_on_sale = models.BooleanField(_("Is On Sale"), default=False)
    retail_price = models.DecimalField(
        _("Retail Price"), default=0, decimal_places=2, max_digits=9
    )
    store_price = models.DecimalField(
        _("Store Price"), default=0, decimal_places=2, max_digits=9
    )
    sale_price = models.DecimalField(
        _("Sale Price"), default=0, decimal_places=2, max_digits=9
    )
    weight = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag, related_name="product_inventory")

    class Meta:
        """
        Meta information for Product objects
        """

        verbose_name = _("Product Inventory")
        verbose_name_plural = _("Product Inventories")

    def __str__(self):
        """
        String representation of Product object
        """
        return f"{self.sku}"
