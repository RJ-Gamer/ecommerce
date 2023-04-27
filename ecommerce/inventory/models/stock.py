"""
Product Model
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .product_inventory import ProductInventory
from .abstract import AbstractTimeStamp


class Stock(AbstractTimeStamp, models.Model):
    """
    Stock Model
    """

    product_inventory = models.OneToOneField(
        ProductInventory, related_name="stock", on_delete=models.CASCADE
    )
    units = models.IntegerField(_("Units"), default=0)
    units_sold = models.IntegerField(_("Units sold"), default=0)

    class Meta:
        """
        Meta information for Product objects
        """

        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")

    def __str__(self):
        """
        String representation of Stock object
        """
        return f"{self.product_inventory}"
