"""
custom backend for login with email or phone
"""
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class PhoneOrEmailBackend(BaseBackend):
    """
    Authenticates a user by their email or phone number.

    Usage:
    1. Add 'PhoneOrEmailBackend' to your AUTHENTICATION_BACKENDS settings.
    2. When logging in, provide either the email or phone number as the username.

    Returns a User object if authentication succeeds, or None if it fails.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticate the user.

        :param request: The current request (unused).
        :param username: The email or phone number of the user.
        :param password: The password entered by the user.
        :param kwargs: Additional keyword arguments (unused).
        :return: A User object if authentication succeeds, or None if it fails.
        """
        try:
            user = User.objects.get(Q(email=username) | Q(phone_number=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Retrieve a User object by ID.

        :param user_id: The ID of the user.
        :return: A User object if it exists, or None if it does not.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
