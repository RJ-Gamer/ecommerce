"""
Url path config for store app
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CreateStoreViewSet


router = DefaultRouter()

router.register("sign-up", CreateStoreViewSet, basename="store-sign-up")

urlpatterns = [
    path("store/", include(router.urls)),
]
