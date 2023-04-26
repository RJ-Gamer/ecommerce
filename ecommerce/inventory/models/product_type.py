"""
Product Type Model
"""
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .product_attribute import ProductAttribute


class ProductType(models.Model):
    """
    Product Type Model
    """

    title = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(_("Slug"), null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    product_type_attributes = models.ManyToManyField(
        ProductAttribute, related_name="product_types", through="ProductTypeAttribute"
    )

    class Meta:
        """
        Meta information for Product objects
        """

        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        """
        String representation of Product object
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
