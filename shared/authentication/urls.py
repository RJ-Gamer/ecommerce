"""
Url path config for authentication app
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    LoginViewSet,
    # ChangePasswordViewSet,
    # RequestOTPViewSet,
    # SetForgotPasswordViewSet,
    # SignUpViewSet,
)

router = DefaultRouter()

router.register("login", LoginViewSet, basename="login")
# router.register("change-password", ChangePasswordViewSet, basename="change-password")
# router.register("request-otp", RequestOTPViewSet, basename="request-otp")
# router.register(
#     "set-forgot-password", SetForgotPasswordViewSet, basename="set-forgot-password"
# )
# router.register("sign-up", SignUpViewSet, basename="sign-up")

urlpatterns = [
    path("auth/", include(router.urls)),
]
