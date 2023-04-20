"""
Change password view for logged in users
"""
import logging
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from shared.authentication.serializers import ChangePasswordSerializer
from shared.utils import messages

log = logging.getLogger(__name__)


class ChangePasswordViewSet(viewsets.ViewSet):
    """
    Change password for a logged in user
    """

    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request):
        """
        POST: Change password

        Changes the password for the logged in user. Requires the old password and new password
        to be provided in the request body.

        Parameters:
        request (rest_framework.request.Request): The HTTP request object

        Sample request body:
        {
            "current_password": "myoldpassword",
            "new_password": "mynewpassword",
            "confirm_password": "mynewpassword"
        }

        Returns:
        rest_framework.response.Response: The HTTP response object
        """
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        log.info(messages.LOG_CHANGE_PSWD.format(request.user))
        return Response(
            {"message": messages.MSG_CHANGE_PSWD}, status=status.HTTP_205_RESET_CONTENT
        )
