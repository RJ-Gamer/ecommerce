"""
Sign Up View
"""
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import status, viewsets
from rest_framework.response import Response

from shared.utils import messages
from shared.authentication.serializers import SignUpSerializer

User = get_user_model()


class SignUpViewSet(viewsets.ViewSet):
    """
    Sign Up View Set
    """

    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        """
        Post request
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": _(messages.MSG_SIGN_UP),
                "data": serializer.data,
                "error": False,
            },
            status=status.HTTP_201_CREATED,
        )
