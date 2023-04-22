"""
verify store serializer
"""
from django.core.validators import RegexValidator

from rest_framework import serializers

from ecommerce.stores.models import Store
from shared.utils.constants import OTP_LENGTH
from shared.utils import messages


class VerifyStoreSerializer(serializers.Serializer):
    """
    verify store serializer
    """

    store_id = serializers.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex="^.{12}$", message=messages.ERR_STORE_ID, code="nomatch"
            )
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
            store = Store.objects.get(store_id=store_id, owner=user)
        except Store.DoesNotExist:
            raise serializers.ValidationError(
                {"store_id": messages.ERR_STORE_NOT_FOUND}
            )
        if user.verify_otp(otp=otp):
            attrs["store"] = store
            return attrs
        raise serializers.ValidationError({"otp": messages.ERR_INVALID_OTP})

    def create(self, validated_data):
        """
        verify store otp
        """
        store = validated_data.get("store")
        store.is_verified = True
        store.save()
        return store
