"""
Admin interface for store
"""
from django.contrib import admin
from ecommerce.stores.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """
    Admin interface for store
    """

    list_display = ["id", "title", "store_id", "is_verified", "created_at"]
    list_display_links = ["id", "title", "store_id"]
    list_filter = ["is_verified", "created_at", "updated_at"]
    search_fields = ["title", "description", "store_id"]
    readonly_fields = ["store_id", "created_at", "updated_at"]
    fieldsets = [
        [
            "Details",
            {
                "fields": [
                    "title",
                    "store_id",
                    "owner",
                    "description",
                ]
            },
        ],
        ["Flags", {"fields": ["is_verified"]}],
        ["Dates", {"fields": ["created_at", "updated_at"]}],
    ]
