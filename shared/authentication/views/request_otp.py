"""
Request OTP View
"""
from django.utils.translation import gettext_lazy as _

from rest_framework import status, viewsets
from rest_framework.response import Response

from shared.utils import messages
from shared.authentication.serializers import RequestOTPSerializer


class RequestOTPViewSet(viewsets.ViewSet):
    """
    Request otp viewsets
    """

    serializer_class = RequestOTPSerializer

    def create(self, request):
        """
        Post request
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": _(messages.MSG_OTP_SENT)}, status=status.HTTP_200_OK
        )
