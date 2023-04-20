"""
App Config for authentication
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    App Config for authentication
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "shared.authentication"

    def ready(self) -> None:
        from . import signals
