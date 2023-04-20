"""
Set forgot password view
"""
import logging

from django.utils.translation import gettext_lazy as _

from rest_framework import status, viewsets
from rest_framework.response import Response

from shared.utils import messages
from shared.authentication.serializers import SetForgotPasswordSerializer

log = logging.getLogger(__name__)


class SetForgotPasswordViewSet(viewsets.ViewSet):
    """
    Set forgot password view
    """

    serializer_class = SetForgotPasswordSerializer

    def create(self, request):
        """
        Post request
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        log.info(messages.LOG_CHANGE_PSWD.format(user))
        return Response(
            {"message": _(messages.MSG_CHANGE_PSWD), "error": False},
            status=status.HTTP_205_RESET_CONTENT,
        )
