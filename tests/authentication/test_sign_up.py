"""
Test cases for sign up
"""
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from shared.authentication.models import UserSecretInfo
from shared.utils import messages
from tests import routes, dummies

User = get_user_model()


class SignUpTestCase(APITestCase):
    """
    Test cases for sign up
    """

    def setUp(self) -> None:
        self.url = routes.SIGN_UP

    def test_signup_valid_minimum_data(self):
        """
        Valid test case with minimum input
        """
        data = {
            "email": dummies.VALID_EMAIL_1,
            "password": dummies.VALID_PSWD,
            "confirm_password": dummies.VALID_PSWD,
        }
        response = self.client.post(routes.SIGN_UP, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["data"]["email"], dummies.VALID_EMAIL_1)

    def test_signup_valid_maximum_data(self):
        """
        Valid test case with minimum input
        """
        data = {
            "email": dummies.VALID_EMAIL_1,
            "password": dummies.VALID_PSWD,
            "confirm_password": dummies.VALID_PSWD,
            "first_name": "Test",
            "last_name": "Test",
            "phone_number": "+919809809809",
            "gender": "MALE",
        }
        response = self.client.post(routes.SIGN_UP, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["data"]["gender"], "MALE")

    def test_signup_mismatch_passwords(self):
        """
        Valid test case with minimum input
        """
        data = {
            "email": dummies.VALID_EMAIL_1,
            "password": dummies.VALID_PSWD + "1",
            "confirm_password": dummies.VALID_PSWD,
        }
        response = self.client.post(routes.SIGN_UP, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["password"], [messages.ERR_PSWD_MISMATCH])
