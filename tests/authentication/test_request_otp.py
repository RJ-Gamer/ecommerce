"""
Test cases for request otp
"""
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from shared.utils import messages
from shared.authentication.models import UserSecretInfo
from tests import routes, dummies


User = get_user_model()


class RequestOTPTestCase(APITestCase):
    """
    Test cases for request otp
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1, password=dummies.VALID_PSWD, is_active=True
        )
        self.url = routes.REQUEST_OTP

    def test_valid_request_otp(self):
        """
        Test valid otp trquest
        """
        data = {"username": dummies.VALID_EMAIL_1}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], messages.MSG_OTP_SENT)
        self.assertFalse(self.user.secret.otp, None)

    def test_request_otp_with_invalid_email(self):
        """
        Test valid otp request
        """
        data = {"username": dummies.VALID_EMAIL_2}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["username"],
            [messages.ERR_USER_NOT_FOUND],
        )
