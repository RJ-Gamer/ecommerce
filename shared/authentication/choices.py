"""
Choice Field Classes for Project
"""
from django.utils.translation import gettext_lazy as _
from django.db import models


class GenderChoice(models.TextChoices):
    """
    Gender Choice
    """

    MALE = _("MALE"), "MALE"
    FEMALE = _("FEMALE"), "FEMALE"
    OTHER = _("OTHER"), "OTHER"
    NONE = _("NONE"), "NONE"
