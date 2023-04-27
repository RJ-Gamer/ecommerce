"""
Category Model
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from .abstract import AbstractTimeStamp

class Category(AbstractTimeStamp, models.Model):
    """
    Category Model
    """

    title = models.CharField(_("Title"), max_length=100, unique=True, db_index=True)
    slug = models.SlugField(
        _("Slug"), max_length=100, unique=True, null=True, blank=True
    )
    description = models.TextField(_("Description"), null=True, blank=True)
    image = models.ImageField(
        _("Category Image"), null=True, blank=True, upload_to="categories"
    )

    class Meta:
        """
        Meta information for category
        """

        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        """
        Str representation of category
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
