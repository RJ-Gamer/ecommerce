"""
verify store serializer
"""
from django.core.validators import RegexValidator

from rest_framework import serializers

from ecommerce.stores.models import Store
from shared.utils.constants import STORE_CODE_HELP_TXT, OTP_LENGTH
from shared.utils import messages


class VerifyStoreSerializer(serializers.Serializer):
    """
    verify store serializer
    """

    store_id = serializers.CharField(
        max_length=12,
        validators=[
            RegexValidator(regex="^.{12}$", message=STORE_CODE_HELP_TXT, code="nomatch")
        ],
    )
    otp = serializers.CharField(max_length=OTP_LENGTH)

    def validate(self, attrs):
        """
        Validate the attrs
        """
        otp = attrs.get("otp")
        store_id = attrs.get("store_id")
        user = self.context.get("user")
        try:
            store = Store.objects.get(store_id=store_id)
        except Store.DoesNotExist:
            raise serializers.ValidationError(
                {"store_id": messages.ERR_STORE_NOT_FOUND}
            )
        if user.verify_otp(otp=otp):
            store.is_verified = True
            store.save()
