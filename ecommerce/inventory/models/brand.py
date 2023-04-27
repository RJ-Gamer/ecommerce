"""
Brand Model
"""
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .abstract import AbstractModel, AbstractTimeStamp
from .tag import Tag
from .category import Category


class Brand(AbstractModel, AbstractTimeStamp, models.Model):
    """
    Brand Model
    """

    title = models.CharField(max_length=255, db_index=True, unique=True)
    image = models.ImageField(
        _("Brand Image"), null=True, blank=True, upload_to="brands"
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="brands",
        on_delete=models.SET_NULL,
    )
    tags = models.ManyToManyField(Tag, related_name="brands")

    class Meta:
        """
        Meta information for brand
        """

        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        """
        String representation of the brand object
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
