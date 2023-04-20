"""
Signals for user app
"""
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from shared.authentication.models import UserSecretInfo


@receiver(post_save, sender=get_user_model())
# pylint: disable=unused-argument
def create_secret_profile(sender, instance, created, **kwargs):
    """
    Create a new secret profile for newly created user
    """
    if created:
        UserSecretInfo.objects.create(user=instance)
