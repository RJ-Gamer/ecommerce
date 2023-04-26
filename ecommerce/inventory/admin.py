"""
Admin interface for inventory
"""
from django.contrib import admin
from .models import Tag, Category, Product


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin interface for Tag model
    """

    list_display = ["id", "title", "slug"]
    list_display_links = ["id", "title", "slug"]
    search_fields = ["title", "slug"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for category
    """

    list_display = ["id", "title", "is_active"]
    list_display_links = ["id", "title"]
    search_fields = ["title", "description"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for Product
    """

    list_display = ["id", "title", "uid", "category", "is_active"]
    list_display_links = ["id", "title", "uid"]
    search_fields = ["slug", "title", "description"]
