"""
Tests for Login View
"""
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from tests import routes, dummies
from shared.utils import messages

User = get_user_model()


class LoginViewSetTestCase(APITestCase):
    """
    test cases for login
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1,
            phone_number=dummies.VALID_PHONE_NUM,
            password=dummies.VALID_PSWD,
            is_active=True,
        )
        self.url = routes.LOGIN

    def test_login_success(self):
        """
        test login success with email and password
        """
        data = {"username": dummies.VALID_EMAIL_1, "password": dummies.VALID_PSWD}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["error"], False)

    def test_login_success_with_phone(self):
        """
        test login success with phone and password
        """
        data = {"username": dummies.VALID_PHONE_NUM, "password": dummies.VALID_PSWD}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["error"], False)

    def test_login_with_inactive_user(self):
        """
        test login success
        """
        user = User.objects.create_user(
            email=dummies.VALID_EMAIL_2, password=dummies.VALID_PSWD, is_active=False
        )
        data = {"username": dummies.VALID_EMAIL_2, "password": dummies.VALID_PSWD}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["inactive"], [messages.ERR_INACTIVE_USER])

    def test_login_with_invalid_credentials(self):
        """
        test with invalid credentials
        """
        data = {
            "username": dummies.INVALID_EMAIL_1,
            "password": dummies.INVALID_PSWD,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["credentials"], [messages.ERR_INVALID_CREDS])

    def test_login_without_credentials(self):
        """
        test without credentials
        """
        data = {
            "username": None,
            "password": None,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["username"],
            [messages.ERR_NULL_FIELD],
        )
        self.assertEqual(response.data["password"], [messages.ERR_NULL_FIELD])
