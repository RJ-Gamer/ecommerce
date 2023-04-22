"""
test cases for store verify
"""
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from tests import routes, dummies
from shared.utils import messages, functions
from ecommerce.stores.models import Store

User = get_user_model()


class VerifyStoreTestCase(APITestCase):
    """
    test cases for store verify
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1, password=dummies.VALID_PSWD, is_active=True
        )
        self.store = Store.objects.create(
            title="Test Store", owner=self.user, store_id="123456789012"
        )
        self.otp = functions.generate_otp()
        self.user.set_otp(otp=self.otp)
        self.url = routes.STORE_VERIFY
        self.token = str(RefreshToken.for_user(self.user).access_token)

    # Tests that a valid request data is provided and the store verification is successful.
    def test_successful_store_verification(self):
        """
        Tests that a valid request data is provided and the store verification is successful.
        """
        data = {"store_id": "123456789012", "otp": self.otp}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == messages.MSG_STORE_VERIFIED
        assert response.data["error"] is False
        assert response.data["data"]["user"] == str(self.user)

    # Tests that an invalid store ID is provided.
    def test_invalid_length_store_id(self):
        """
        Tests that an invalid store ID is provided.
        """
        data = {"store_id": "12345", "otp": self.otp}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["store_id"] == [messages.ERR_STORE_ID]

    def test_invalid_store_id(self):
        """
        Tests that an invalid store ID is provided.
        """
        data = {"store_id": "123456789014", "otp": self.otp}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["store_id"] == [messages.ERR_STORE_NOT_FOUND]

    # Tests that an invalid OTP is provided.
    def test_invalid_otp(self):
        """
        Tests that an invalid OTP is provided.
        """
        data = {"store_id": "123456789012", "otp": "123456"}
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.post(self.url, data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["otp"] == [messages.ERR_INVALID_OTP]
