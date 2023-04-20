"""
This module contains RequestOTPSerializer for requesting OTP for password reset.
"""
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from shared.utils import messages, functions, constants
from shared.utils.email import EmailThread

User = get_user_model()


class RequestOTPSerializer(serializers.Serializer):
    """
    Serializer for requesting OTP for password reset.
    """

    username = serializers.CharField(help_text="User's email or phone number.")

    def validate(self, attrs):
        """
        Validate the attributes.
        :param attrs: Dictionary of attributes.
        :return: Validated attributes.
        :raises: ValidationError if the user is not found or if the email fails to send.
        """

        username = attrs.get("username")
        try:
            user = User.objects.get(Q(email=username) | Q(phone_number=username))
            otp = functions.generate_otp(constants.OTP_LENGTH)
            user.set_otp(otp=otp)
            mail = EmailThread(
                subject=constants.FORGOT_PSWD_MAIL_SUBJECT,
                template_name="request_otp.html",
                context={
                    "subject": constants.FORGOT_PSWD_MAIL_SUBJECT,
                    "otp": otp,
                    "validity": 10,
                },
            )
            mail.send_one_email(to_email=user.email)
            attrs["user"] = user
            return attrs
        except User.DoesNotExist:
            raise ValidationError({"username": _(messages.ERR_USER_NOT_FOUND)})
        except Exception as error:
            raise ValidationError({"email": _(messages.ERR_EMAIL_FAILED.format(error))})
