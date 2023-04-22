"""
viewset for store verification
"""
import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from shared.utils import constants, email, messages
from ecommerce.stores.serializers import VerifyStoreSerializer

log = logging.getLogger(__name__)


class VerifyStoreViewSet(viewsets.ViewSet):
    """
    store verification view
    """

    serializer_class = VerifyStoreSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        post request
        """
        serializer = self.serializer_class(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        mail = email.EmailThread(
            subject=constants.STORE_VERIFIED_EMAIL_SUBJECT,
            template_name="store_verified.html",
            context={"user": request.user},
        )
        mail.send_one_email(request.user.email)
        serializer.save()
        log.info(messages.LOG_STORE_VERIFIED.format(request.user))
        return Response(
            {
                "message": messages.MSG_STORE_VERIFIED,
                "error": False,
                "data": {
                    "user": str(request.user),
                    "store": request.user.store.title,
                    "store_id": request.user.store.store_id,
                },
            },
            status=status.HTTP_200_OK,
        )
