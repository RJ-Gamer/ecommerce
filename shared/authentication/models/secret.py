"""
User Secret info Model
"""
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserSecretInfo(models.Model):
    """
    Model for storing user's secret information, including One Time Password (OTP)
    """

    user = models.OneToOneField(
        User,
        related_name="secret",
        on_delete=models.CASCADE,
    )
    otp = models.CharField(_("Otp"), max_length=100, null=True, blank=True)
    otp_created_at = models.DateTimeField(
        _("Otp Created At"),
        null=True,
        blank=True,
    )
    otp_expires_at = models.DateTimeField(_("Otp Expiry"), null=True, blank=True)
    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
        help_text="The date and time this secret information was last updated.",
    )

    def __str__(self):
        """
        Returns a string representation of the UserSecretInfo object.
        """
        return f"{self.user}"
