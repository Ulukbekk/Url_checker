from django.shortcuts import render
from rest_framework import generics, permissions

from users.serializers import AccountRegistrationSerializer


class AccountRegisterAPIView(generics.CreateAPIView):
    """
    This endpoint registers users based on the fields
    """
    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)
