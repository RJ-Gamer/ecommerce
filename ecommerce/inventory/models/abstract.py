"""
Abstract classes
"""
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shared.utils.functions import generate_unique_code
from shared.utils import constants


class AbstractModel(models.Model):
    """
    Common Fields
    """

    uid = models.CharField(
        _("Product UID"),
        max_length=16,
        unique=True,
        db_index=True,
        editable=False,
        default=generate_unique_code(length=constants.PRODUCT_UID_LEN),
    )
    slug = models.SlugField(_("Slug"), null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)

    class Meta:
        """
        Meta information
        """

        abstract = True


class AbstractTimeStamp(models.Model):
    """
    Time Stamps model
    """

    is_active = models.BooleanField(_("Is active"), default=False)
    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=timezone.now)

    class Meta:
        """
        Meta information
        """

        abstract = True
