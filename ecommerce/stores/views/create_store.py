"""
store viewset
"""
import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from shared.utils import messages
from ecommerce.stores.serializers import CreateStoreSerializer

log = logging.getLogger(__name__)


class CreateStoreViewSet(viewsets.ViewSet):
    """
    store view set
    """

    serializer_class = CreateStoreSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        """
        post request to store
        """
        serializer = self.serializer_class(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        log.info(messages.LOG_STORE_CREATED.format(request.user))
        return Response(
            {
                "message": messages.MSG_STORE_CREATED,
                "error": False,
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
