"""
This module contains SetForgotPasswordSerializer for setting a new password after validating the OTP.
"""
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from shared.utils import messages, constants

User = get_user_model()


class SetForgotPasswordSerializer(serializers.Serializer):
    """
    Serializer for setting a new password after validating the OTP.
    """

    username = serializers.CharField(help_text="User's email or phone number.")
    otp = serializers.CharField(help_text="The OTP sent to the user.")
    new_password = serializers.CharField(
        min_length=constants.MIN_PSWD_LEN, help_text="The new password."
    )
    confirm_password = serializers.CharField(
        min_length=constants.MIN_PSWD_LEN, help_text="The new password confirmation."
    )

    def validate(self, attrs):
        """
        Validate the attributes.
        :param attrs: Dictionary of attributes.
        :return: Validated attributes.
        :raises: ValidationError if the passwords do not match, the user is not found, or the OTP is invalid.
        """

        username = attrs.get("username")
        otp = attrs.get("otp")
        new_password = attrs.get("new_password")
        confirm_password = attrs.get("confirm_password")

        if new_password != confirm_password:
            raise ValidationError({"passwords": _(messages.ERR_PSWD_MISMATCH)})
        try:
            user = User.objects.get(Q(email=username) | Q(phone_number=username))
            if not user.verify_otp(otp):
                raise ValidationError({"otp": _(messages.ERR_INVALID_OTP)})
            attrs["user"] = user
            return attrs
        except User.DoesNotExist:
            raise ValidationError({"username": _(messages.ERR_USER_NOT_FOUND)})
