"""
Test cases for setting the for got password
"""
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from shared.utils import constants, functions, messages
from shared.authentication.models import UserSecretInfo
from tests import routes, dummies

User = get_user_model()


class SetForgotPasswordTestCase(APITestCase):
    """
    Test cases for setting the forgot password
    """

    def setUp(self):
        self.client = APIClient()
        self.url = routes.SET_FORGOT_PSWD
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1,
            password=dummies.VALID_PSWD,
            phone_number=dummies.VALID_PHONE_NUM,
            is_active=True,
        )
        self.otp = functions.generate_otp()
        self.user.set_otp(otp=self.otp)

    def test_valid_set_password(self):
        """
        Valid conditions for setting forgot password
        """
        data = {
            "username": dummies.VALID_EMAIL_1,
            "otp": self.otp,
            "new_password": dummies.INVALID_PSWD,
            "confirm_password": dummies.INVALID_PSWD,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.user.get_otp, self.otp)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertEqual(response.data["message"], messages.MSG_CHANGE_PSWD)

    def test_set_forgot_password_invalid_data(self):
        """
        Test to check if validation is working as expected for invalid data
        """
        data = {
            "username": dummies.VALID_EMAIL_1,
            "otp": self.otp,
            "new_password": "newtestpassword",
            "confirm_password": "wrongpassword",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["passwords"], [messages.ERR_PSWD_MISMATCH])

    def test_set_forgot_password_invalid_otp(self):
        """
        Test to check if validation is working as expected for invalid OTP
        """
        data = {
            "username": dummies.VALID_EMAIL_1,
            "otp": "654321",
            "new_password": "newtestpassword",
            "confirm_password": "newtestpassword",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["otp"], [messages.ERR_INVALID_OTP])

    def test_set_forgot_password_user_not_found(self):
        """
        Test to check if validation is working as expected for user not found
        """
        data = {
            "username": "invaliduser@example.com",
            "otp": self.otp,
            "new_password": "newtestpassword",
            "confirm_password": "newtestpassword",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["username"], [messages.ERR_USER_NOT_FOUND])

    def test_set_forgot_password_otp_expired(self):
        """
        Test to check if validation is working as expected for expired OTP
        """
        self.user.secret.otp_created_at = timezone.now() - timedelta(minutes=10)
        self.user.secret.otp_expires_at = timezone.now() - timedelta(minutes=5)
        self.user.secret.save()
        data = {
            "username": dummies.VALID_EMAIL_1,
            "otp": self.otp,
            "new_password": "newtestpassword",
            "confirm_password": "newtestpassword",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["otp"], [messages.ERR_INVALID_OTP])
