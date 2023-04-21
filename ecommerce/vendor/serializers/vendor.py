"""
Vendor serializer
"""
from rest_framework import serializers
from ecommerce.vendor.models import Vendor

from shared.utils import functions, constants
from shared.utils.email import EmailThread


class VendorSerializer(serializers.ModelSerializer):
    """
    Vendor serializer
    """

    class Meta:
        """
        Meta information for Vendor serializer
        """

        model = Vendor
        fields = ["id", "owner", "title", "description", "created_at", "updated_at"]

    def validate(self, attrs):
        """
        Validate attrs
        """
        attrs["user"] = self.context.get("user")
        return attrs

    def create(self, validated_data):
        """
        create vendor from validated data
        """
        user = validated_data.pop("user")
        vendor = Vendor.objects.create(owner=user, **validated_data)
        otp = functions.generate_otp()
        mail = EmailThread(
            subject=constants.VENDOR_SIGN_UP_EMAIL_SUBJECT,
            template_name="vendor_signup_otp.html",
            context={"vendor_name": str(vendor.owner), "otp": otp},
        )
        mail.send_one_email(to_email=vendor.owner.email)
        return vendor
