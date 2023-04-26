"""
store model
"""
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

from shared.utils import constants, functions

User = get_user_model()


class Store(models.Model):
    """
    Store model
    """

    store_id = models.CharField(
        _("Store ID"),
        max_length=15,
        unique=True,
        db_index=True,
        editable=False,
        default=functions.generate_unique_code,
    )
    owner = models.OneToOneField(
        User, related_name="store", on_delete=models.PROTECT, null=True, blank=True
    )
    title = models.CharField(
        _("Title"),
        max_length=255,
        help_text="Give a name to your online store",
        unique=True,
        db_index=True,
    )
    slug = models.SlugField(_("Slug"), max_length=255, null=True, blank=True)
    description = models.TextField(
        _("Description"),
        blank=True,
        null=True,
        help_text="Approach potential buyers with catching description",
        max_length=constants.DESCRIPTION_FLD_LEN,
    )
    is_verified = models.BooleanField(_("Verified"), default=False)
    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=timezone.now)

    class Meta:
        """
        Meta information for store
        """

        ordering = ("updated_at",)

    def __str__(self):
        """
        return string representation of the store object
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
