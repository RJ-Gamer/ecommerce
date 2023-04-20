"""
This module contains LoginSerializer for user authentication.
"""

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from shared.utils import messages


class LoginSerializer(serializers.Serializer):
    """
    Serializer for authenticating users.
    """

    username = serializers.CharField(
        help_text="User's email or phone number(with country code)."
    )
    password = serializers.CharField(help_text="User's password.")

    def validate(self, attrs):
        """
        Validate attributes.
        :param attrs: Dictionary of attributes.
        :return: Validated attributes.
        :raises: ValidationError if the user is not active or if the credentials are invalid.
        """

        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                attrs["user"] = user
                return attrs
            raise ValidationError({"inactive": _(messages.ERR_INACTIVE_USER)})
        raise ValidationError({"credentials": _(messages.ERR_INVALID_CREDS)})
