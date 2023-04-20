"""
Manager for creating new users and superusers
"""
import logging

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import BaseUserManager
from shared.utils import messages

log = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """
    Manager for creating new users and superusers
    """

    def create_user(self, email, password=None, **kwargs):
        """
        Create a new user from the given email and password
        """
        if not email:
            raise ValueError(_(messages.ERR_BLANK_FIELD))
        if not password:
            raise ValueError(_(messages.ERR_BLANK_FIELD))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        log.info(messages.LOG_USER_CREATED.format(email))
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Create a new superuser from the given email and password
        """
        user = self.create_user(email, password, **kwargs)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

    def active(self):
        """
        Filter active users and return queryset
        """
        return self.filter(is_active=True)
