"""
Test Cases for change the password
"""
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from tests import routes, dummies
from shared.utils import messages, functions

User = get_user_model()


class AccountVarificationTestCase(APITestCase):
    """
    Test case for Account Varification
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1, password=dummies.VALID_PSWD
        )
        self.otp = functions.generate_otp()
        self.user.set_otp(otp=self.otp)
        self.url = routes.ACCOUNT_VERIFY

    def test_account_variation_success(self):
        """
        test account variation success
        """
        data = {"username": dummies.VALID_EMAIL_1, "otp": self.otp}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], messages.MSG_EMAIL_VERIFIED)

    def test_account_verification_invalid_email(self):
        """
        test account verification with invalid email
        """
        data = {"username": dummies.VALID_EMAIL_2, "otp": self.otp}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["username"], [messages.ERR_USER_NOT_FOUND])

    def test_account_verification_invalid_otp(self):
        """
        test account verification with invalid otp
        """
        data = {"username": dummies.VALID_EMAIL_1, "otp": functions.generate_otp()}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["otp"], [messages.ERR_INVALID_OTP])
