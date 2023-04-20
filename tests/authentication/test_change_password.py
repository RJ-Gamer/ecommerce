"""
Test Cases for change the password
"""
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from tests import routes, dummies
from shared.utils import messages

User = get_user_model()


class ChangePasswordTestCase(APITestCase):
    """
    Test cases for change the password
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1, password=dummies.VALID_PSWD, is_active=True
        )
        self.url = routes.CHANGE_PASSWORD
        self.token = str(RefreshToken.for_user(self.user).access_token)

    def test_change_password_with_valid_data(self):
        """
        Test change password with valid data
        """
        data = {
            "current_password": dummies.VALID_PSWD,
            "new_password": dummies.VALID_PSWD + "1",
            "confirm_password": dummies.VALID_PSWD + "1",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertEqual(response.data["message"], messages.MSG_CHANGE_PSWD)

    def test_change_password_with_mismatch_pswds(self):
        """
        Test change password with mismatching pswds
        """
        data = {
            "current_password": dummies.VALID_PSWD,
            "new_password": dummies.VALID_PSWD + "1",
            "confirm_password": dummies.VALID_PSWD + "2",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["passwords"], [messages.ERR_PSWD_MISMATCH])

    def test_change_password_with_invalid_current_pswd(self):
        """
        Test change password with mismatching pswds
        """
        data = {
            "current_password": dummies.VALID_PSWD + "1",
            "new_password": dummies.VALID_PSWD + "1",
            "confirm_password": dummies.VALID_PSWD + "1",
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["current_password"], [messages.ERR_INVALID_PSWD])

    def test_change_password_without_token(self):
        """
        Test change password with mismatching pswds
        """
        data = {
            "current_password": dummies.VALID_PSWD,
            "new_password": dummies.VALID_PSWD + "1",
            "confirm_password": dummies.VALID_PSWD + "2",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"], messages.ERR_UNAUTHORIZED)
