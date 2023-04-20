"""
Varify Account View
"""
import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from shared.authentication.serializers import AccountVerificationSerializer
from shared.utils import messages

log = logging.getLogger(__name__)


class AccountVerificationViewSet(viewsets.ViewSet):
    """
    Account Verification View
    """

    serializer_class = AccountVerificationSerializer

    def create(self, request):
        """
        POST Request
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        log.info(messages.LOG_EMAIL_VERIFIED.format(user))
        return Response(
            {
                "message": messages.MSG_EMAIL_VERIFIED,
                "error": False,
                "data": {
                    "user": str(user),
                    "is_email_verified": user.is_email_verified,
                    "is_active": user.is_active,
                },
            },
            status=status.HTTP_200_OK,
        )
