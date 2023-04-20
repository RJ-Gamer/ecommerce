"""
Login View
"""
import logging
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from shared.authentication.serializers import LoginSerializer
from shared.utils import messages

log = logging.getLogger(__name__)


class LoginViewSet(viewsets.ViewSet):
    """
    Login View Set
    """

    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles user authentication.

        Returns:
            Response: A JSON response containing user data and access/refresh tokens.

        Example request body:
            {
                "email": "user@example.com",
                "password": "password123"
            }

        Raises:
            ValidationError: If the provided data is invalid.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token = RefreshToken.for_user(user)
        log.info(messages.LOG_LOGIN_SUCCESS.format(user))
        return Response(
            {
                "message": _(messages.MSG_LOGIN_SUCCESS.format(user)),
                "data": {
                    "user_id": user.id,
                    "email": user.email,
                    "refresh": str(token),
                    "access": str(token.access_token),
                },
                "error": False,
            },
            status=status.HTTP_200_OK,
        )
