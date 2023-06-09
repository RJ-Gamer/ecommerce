"""
Media Model
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from .abstract import AbstractTimeStamp
from .product_inventory import ProductInventory


class Media(AbstractTimeStamp, models.Model):
    """
    Media Model
    """

    product_inventory = models.ForeignKey(
        ProductInventory, related_name="product_media", on_delete=models.CASCADE
    )
    alt_text = models.CharField(
        _("Alt Text"), max_length=255, db_index=True, blank=True, null=True
    )
    image = models.ImageField(_("Image"), upload_to="products")
    is_featured = models.BooleanField(_("Is Featured"), default=False)

    class Meta:
        """
        Meta information for Product objects
        """

        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        """
        String representation of Product object
        """
        return f"{self.alt_text}"
