"""
Module containing ChangePasswordSerializer for Logged in Users.
"""
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from shared.utils import constants, messages


class ChangePasswordSerializer(serializers.Serializer):
    """
    Change password serializer for logged in users.

    Attributes:
        current_password (CharField): User's current password.
        new_password (CharField): User's new password.
        confirm_password (CharField): User's new password confirmation.
    """

    current_password = serializers.CharField()
    new_password = serializers.CharField(min_length=constants.MIN_PSWD_LEN)
    confirm_password = serializers.CharField(min_length=constants.MIN_PSWD_LEN)

    def validate(self, attrs):
        """
        Validates the provided data.

        Args:
            attrs (dict): The data provided by the user.

        Returns:
            dict: The validated data.

        Raises:
            ValidationError: If the provided data is invalid.
        """
        user = self.context["request"].user
        current_password = attrs.get("current_password")
        new_password = attrs.get("new_password")
        confirm_password = attrs.get("confirm_password")

        # check if current password is correct
        if not user.check_password(current_password):
            raise ValidationError({"current_password": messages.ERR_INVALID_PSWD})
        if new_password != confirm_password:
            raise ValidationError({"passwords": messages.ERR_PSWD_MISMATCH})
        user.set_password(new_password)
        user.save()
        return attrs
