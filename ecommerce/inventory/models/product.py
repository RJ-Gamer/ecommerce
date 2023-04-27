"""
Product Model
"""
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .abstract import AbstractModel, AbstractTimeStamp
from .tag import Tag
from .category import Category


class Product(AbstractModel, AbstractTimeStamp, models.Model):
    """
    Product Model
    """

    title = models.CharField(max_length=255, db_index=True)
    tags = models.ManyToManyField(Tag, related_name="products")
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="products",
        on_delete=models.SET_NULL,
    )

    class Meta:
        """
        Meta information for Product objects
        """

        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        """
        String representation of Product object
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
