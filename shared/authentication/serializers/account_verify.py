"""
Account Verification serializer
"""
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework import serializers

from shared.utils import messages

User = get_user_model()


class AccountVerificationSerializer(serializers.Serializer):
    """
    Account Verification serializer
    """

    username = serializers.CharField(
        help_text="Enter your email address or phone number with country code. Ex: +919876543210"
    )
    otp = serializers.CharField()

    def validate(self, attrs):
        """
        validate the attrs
        """
        username = attrs.get("username")
        otp = attrs.get("otp")

        try:
            user = User.objects.get(Q(email=username) | Q(phone_number=username))
            attrs["user"] = user
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"username": _(messages.ERR_USER_NOT_FOUND)}
            )
        if user.verify_otp(otp=otp):
            user.is_active = True
            user.is_email_verified = True
            user.save()
            return attrs
        raise serializers.ValidationError({"otp": _(messages.ERR_INVALID_OTP)})
