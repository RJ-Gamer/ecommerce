"""
Admin interface for authentication models
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib.auth import get_user_model
from shared.authentication.models import UserSecretInfo

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseAdmin):
    """
    Admin interface for Users
    """

    list_display = ["id", "__str__", "email", "gender", "is_active"]
    list_display_links = ["id", "__str__", "email"]
    list_filter = ["is_active", "gender"]
    search_fields = ["__str__", "email"]
    readonly_fields = ["uid", "created_at", "updated_at"]
    ordering = ["id", "email"]

    fieldsets = [
        ["Credentials", {"fields": ["uid", "email", "password"]}],
        [
            "Detail",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "gender",
                    "phone_number",
                    "created_at",
                    "updated_at",
                ]
            },
        ],
        ["Flags", {"fields": ["is_active", "is_staff", "is_superuser"]}],
        ["Permissions", {"fields": ["groups", "user_permissions"]}],
    ]
    add_fieldsets = [
        ["Credentials", {"fields": ["email", "password1", "password2"]}],
        [
            "Detail",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "gender",
                    "phone_number",
                ]
            },
        ],
        ["Flags", {"fields": ["is_active", "is_staff", "is_superuser"]}],
        ["Permissions", {"fields": ["groups", "user_permissions"]}],
    ]


admin.site.register(UserSecretInfo)
