"""
Vendor viewset
"""
import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from shared.utils import messages
from ecommerce.vendor.serializers import VendorSerializer

log = logging.getLogger(__name__)


class VendorCreateViewSet(viewsets.ViewSet):
    """
    Vendor view set
    """

    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        """
        post request to vendor
        """
        serializer = self.serializer_class(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        log.info(messages.LOG_VENDOR_CREATED.format(request.user))
        return Response(
            {
                "message": messages.MSG_VENDOR_CREATED,
                "error": False,
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
