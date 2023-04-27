"""
Url path config for store app
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    GetProductInventoryListViewSet,
)


router = DefaultRouter()

router.register("products", GetProductInventoryListViewSet, basename="products")

urlpatterns = [
    path("inventory/", include(router.urls)),
]
