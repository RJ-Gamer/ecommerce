"""
Vendor model
"""
import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from shared.utils import constants

User = get_user_model()


class Vendor(models.Model):
    """
    Vendor models
    """

    vendor_uid = models.UUIDField(
        unique=True, db_index=True, editable=False, default=uuid.uuid4
    )
    owner = models.OneToOneField(
        User, related_name="vendor", on_delete=models.PROTECT, null=True, blank=True
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
        _("Created At"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        """
        Meta information for Vendor
        """

        ordering = ("updated_at",)

    def __str__(self):
        """
        return string representation of the vendor object
        """
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
