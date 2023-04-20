"""
User Model
"""
import uuid
from datetime import timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

from shared.authentication.choices import GenderChoice
from shared.authentication.managers import UserManager
from shared.utils import constants


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model class
    """

    uid = models.UUIDField(
        unique=True, db_index=True, editable=False, default=uuid.uuid4
    )
    email = models.EmailField(
        _("Email ID"),
        unique=True,
        db_index=True,
        max_length=100,
    )
    phone_number = PhoneNumberField(
        _("Phone number"),
        unique=True,
        db_index=True,
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        _("First name"), max_length=100, null=True, blank=True
    )
    last_name = models.CharField(
        _("Last name"),
        max_length=100,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        _("Gender"),
        max_length=100,
        choices=GenderChoice.choices,
        default=GenderChoice.NONE,
    )

    is_active = models.BooleanField(_("Is Active"), default=False)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)
    is_email_verified = models.BooleanField(_("Email verified"), default=False)

    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """
        Metadata for User object
        """

        ordering = ["id", "email"]

    def __str__(self) -> str:
        """
        Returns the string representation of a User object
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def get_otp(self):
        """
        Get OTP for a user
        :return: OTP
        """
        return self.secret.otp

    def set_otp(self, otp=None):
        """
        Set OTP for a user
        :param otp: OTP to be set
        """
        if otp:
            self.secret.otp = otp
            self.secret.otp_created_at = timezone.now()
            self.secret.otp_expires_at = timezone.now() + timedelta(
                minutes=constants.OTP_EXPIRE_IN_MIN
            )
        else:
            self.secret.otp = otp
            self.secret.otp_created_at = None
            self.secret.otp_expires_at = None
        self.secret.save()

    def verify_otp(self, otp):
        """
        Verify OTP for a user
        :param otp: OTP to be verified
        :return: True if OTP is verified else False
        """
        if self.secret.otp != otp:
            return False
        if self.secret.otp_expires_at < timezone.now():
            return False
        self.set_otp(otp=None)
        return True
