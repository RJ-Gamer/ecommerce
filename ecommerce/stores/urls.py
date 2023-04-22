"""
Url path config for store app
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CreateStoreViewSet, VerifyStoreViewSet


router = DefaultRouter()

router.register("sign-up", CreateStoreViewSet, basename="store-sign-up")
router.register("verify-store", VerifyStoreViewSet, basename="verify-store")

urlpatterns = [
    path("store/", include(router.urls)),
]
