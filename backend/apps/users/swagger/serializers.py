from rest_framework import serializers

from apps.auth.swagger.serializers import SwaggerUserSerializer


class SwaggerUserList(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    prev = serializers.CharField()
    next = serializers.CharField()
    page = serializers.IntegerField()
    data = SwaggerUserSerializer(many=True)
