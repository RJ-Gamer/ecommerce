"""
test cases for vendor create
"""
import logging
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests import routes, dummies
from shared.utils import messages

User = get_user_model()


class VendorCreateTestCase(APITestCase):
    """
    test cases for creating new vendor
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_1, password=dummies.VALID_PSWD, is_active=True
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_valid_request_data_inactive_user_creates_vendor(self):
        """
        Shiver me timbers! This test checks if valid request data with inactive user.
        """
        self.user = User.objects.create_user(
            email=dummies.VALID_EMAIL_2, password=dummies.VALID_PSWD
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        data = {"title": "Test Vendor", "description": "This is a test vendor."}
        response = self.client.post(routes.VENDOR_CREATE, data=data, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["detail"] == messages.ERR_USER_INACTIVE

    # Tests that valid request data creates a vendor successfully.
    def test_valid_request_data_creates_vendor(self):
        """
        Shiver me timbers! This test checks if valid request data creates a vendor successfully.
        """
        data = {"title": "Test Vendor", "description": "This is a test vendor."}
        response = self.client.post(routes.VENDOR_CREATE, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["error"] is False
        assert response.data["message"] == messages.MSG_VENDOR_CREATED

    # Tests that an unauthenticated user cannot create a vendor.
    def test_unauthenticated_user(self):
        """
        Ahoy! This test checks if an unauthenticated user cannot create a vendor.
        """
        client = APIClient()
        data = {"title": "Test Vendor", "description": "This is a test vendor."}
        response = client.post(routes.VENDOR_CREATE, data=data, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["detail"] == messages.ERR_UNAUTHORIZED

    # Tests that missing required fields result in a validation error.
    def test_missing_required_fields(self):
        """
        Aye aye! This test checks if missing required fields result in a validation error.
        """
        data = {"description": "This is a test vendor."}
        response = self.client.post(routes.VENDOR_CREATE, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] == [messages.ERR_BLANK_FIELD]
