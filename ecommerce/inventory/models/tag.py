"""
Tags model
"""
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    """
    Tag model
    """

    title = models.CharField(_("Title"), max_length=100, unique=True, db_index=True)
    slug = models.SlugField(
        _("Slug"), max_length=100, unique=True, blank=True, null=True
    )

    class Meta:
        """
        Meta information for Tag model
        """

        ordering = ("-id",)

    def __str__(self) -> str:
        return f"{self.title}"

    def set_title(self, value):
        """
        Update the title with all lowercase
        """
        self.title = value.lower()

    def get_title(self):
        """
        Get the title
        """
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.title = str(self.get_title().lower())
        super().save(*args, **kwargs)
