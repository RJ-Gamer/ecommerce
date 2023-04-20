"""
Test cases for emails
"""
from rest_framework.test import APITestCase
from shared.utils.email import EmailThread
from tests.dummies import VALID_EMAIL_1


class EmailThreadTestCase(APITestCase):
    """
    Test cases for email thread class
    """

    def test_send_one_email_valid_params(self):
        """
        Tests that an email is sent successfully with valid parameters.
        """
        email_thread = EmailThread(
            subject="Test Email",
            body="This is a test email.",
            from_email="test@example.com",
        )
        result = email_thread.send_one_email(VALID_EMAIL_1)
        assert result == True