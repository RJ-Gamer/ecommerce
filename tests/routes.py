"""
Url routes for tests
"""
from django.urls import reverse

# Authentication app
LOGIN = reverse("login-list")
CHANGE_PASSWORD = reverse("change-password-list")
REQUEST_OTP = reverse("request-otp-list")
