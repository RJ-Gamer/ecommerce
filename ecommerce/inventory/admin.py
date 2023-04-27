"""
Admin interface for inventory
"""
from django.contrib import admin
from .models import (
    Tag,
    Category,
    Product,
    Brand,
    ProductAttribute,
    ProductType,
    ProductAttributeValue,
    ProductInventory,
    Media,
    Stock,
    ProductTypeAttribute,
    ProductAttributeValues,
)


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


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Admin interface for Product
    """

    list_display = ["id", "title", "uid", "category", "is_active"]
    list_display_links = ["id", "title", "uid"]
    search_fields = ["slug", "title", "description"]


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    """
    Admin interface for Product
    """

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["slug", "title", "description"]


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    Admin interface for Product
    """

    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["slug", "title", "description"]


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    """
    Admin interface for Product
    """

    list_display = ["id", "product_attribute", "value"]
    list_display_links = ["id", "product_attribute", "value"]
    search_fields = ["product_attribute", "value"]


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Product Inventory
    """

    list_display = ["id", "sku", "uid", "product_type", "product", "brand"]
    list_display_links = ["id", "sku", "uid"]
    search_fields = ["id", "sku", "uid", "product"]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    """
    Media Admin
    """

    list_display = ["id", "alt_text", "product_inventory", "is_active", "is_featured"]
    list_display_links = ["id"]
    search_fields = ["alt_text"]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """
    Stock Admin
    """

    list_display = ["id", "product_inventory", "units", "units_sold"]


admin.site.register(ProductAttributeValues)
admin.site.register(ProductTypeAttribute)
