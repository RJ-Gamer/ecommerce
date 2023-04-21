"""
Url routes for tests
"""
from django.urls import reverse

# Authentication app
LOGIN = reverse("login-list")
CHANGE_PASSWORD = reverse("change-password-list")
REQUEST_OTP = reverse("request-otp-list")
SET_FORGOT_PSWD = reverse("set-forgot-password-list")
SIGN_UP = reverse("sign-up-list")
ACCOUNT_VERIFY = reverse("account-verification-list")

# VENDOR
VENDOR_CREATE = reverse("vendor-sign-up-list")
