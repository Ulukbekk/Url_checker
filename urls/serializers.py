from rest_framework import serializers

from urls.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('link',
                  'status',)


class UrlListSerializer(serializers.ModelSerializer):
    account = serializers.StringRelatedField(many=False)

    class Meta:
        model = Url
        fields = ('id', 'link', 'status', 'account',)