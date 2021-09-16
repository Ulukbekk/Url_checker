import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from urls.models import Url
from urls.permissions import IsOwner
from urls.serializers import UrlSerializer, UrlListSerializer
from urls.services import get_status_code
from users.models import Account


@csrf_exempt
@api_view(['POST'])
def url_add_view(request):
    if request.method == 'POST':
        link = str('http://www.') + request.POST.get('link')
        user = request.user
        account = Account.objects.filter(username=user).first()
        r = get_status_code(link)
        url = Url.objects.create(
            link=link,
            status=r,
            account=account
        )
    return HttpResponse(url, status=status.HTTP_200_OK)


class ListUrlsAPIView(generics.ListAPIView):
    serializer_class = UrlListSerializer
    queryset = Url.objects.all()
    permission_classes = (permissions.AllowAny,)



