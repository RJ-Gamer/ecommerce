"""
store serializer
"""
from rest_framework import serializers
from ecommerce.stores.models import Store

from shared.utils import functions, constants
from shared.utils.email import EmailThread


class CreateStoreSerializer(serializers.ModelSerializer):
    """
    store serializer
    """

    class Meta:
        """
        Meta information for store serializer
        """

        model = Store
        fields = [
            "id",
            "store_id",
            "owner",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        """
        Validate attrs
        """
        attrs["user"] = self.context.get("user")
        return attrs

    def create(self, validated_data):
        """
        create store from validated data
        """
        user = validated_data.pop("user")
        store = Store.objects.create(owner=user, **validated_data)
        otp = functions.generate_otp()
        user.set_otp(otp)
        mail = EmailThread(
            subject=constants.STORE_SIGN_UP_EMAIL_SUBJECT,
            template_name="store_signup_otp.html",
            context={
                "owner_name": str(store.owner),
                "otp": otp,
                "store_id": store.store_id,
            },
        )
        mail.send_one_email(to_email=store.owner.email)
        return store
