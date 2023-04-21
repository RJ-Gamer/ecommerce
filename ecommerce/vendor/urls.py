"""
Url path config for vendor app
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import VendorCreateViewSet


router = DefaultRouter()

router.register("sign-up", VendorCreateViewSet, basename="vendor-sign-up")

urlpatterns = [
    path("vendor/", include(router.urls)),
]
