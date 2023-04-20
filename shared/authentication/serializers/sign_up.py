"""
Sign Up Serializer
"""
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from shared.utils import constants, functions, messages
from shared.utils.email import EmailThread

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    """
    Sign Up serializer
    """

    confirm_password = serializers.CharField(
        write_only=True, min_length=constants.MIN_PSWD_LEN
    )
    password = serializers.CharField(
        write_only=True,
        min_length=constants.MIN_PSWD_LEN,
    )

    class Meta:
        """
        Meta information for serialization
        """

        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "gender",
            "password",
            "confirm_password",
            "created_at",
        )

    def validate(self, attrs):
        """
        Validate attrs
        """
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        if password != confirm_password:
            raise ValidationError({"password": _(messages.ERR_PSWD_MISMATCH)})

        attrs.pop("confirm_password")
        return attrs

    def create(self, validated_data):
        """
        create user from validated data
        """
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        user = User.objects.create_user(
            email=email, password=password, **validated_data
        )
        otp = functions.generate_otp(constants.OTP_LENGTH)
        user.set_otp(otp=otp)
        mail = EmailThread(
            subject=constants.SIGN_UP_MAIL_SUBJECT.format(user),
            template_name="request_otp.html",
            context={
                "user_name": user,
                "otp": otp,
                "validity": 10,
            },
        )
        mail.send_one_email(to_email=user.email)
        return user
