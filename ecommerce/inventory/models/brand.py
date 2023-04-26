"""
Brand Model
"""
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from shared.utils.functions import generate_unique_code
from shared.utils import constants

from .category import Category
from .tag import Tag


class Brand(models.Model):
    """
    Brand Model
    """

    uid = models.CharField(
        _("Brand UID"),
        max_length=16,
        unique=True,
        db_index=True,
        editable=False,
        default=generate_unique_code(length=constants.PRODUCT_UID_LEN),
    )
    title = models.CharField(max_length=255, db_index=True, unique=True)
    slug = models.SlugField(_("Slug"), null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="brands",
        on_delete=models.SET_NULL,
    )
    image = models.ImageField(
        _("Brand Image"), null=True, blank=True, upload_to="brands"
    )
    is_active = models.BooleanField(_("Is active"), default=False)
    tags = models.ManyToManyField(Tag, related_name="brands")
    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=timezone.now)

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
