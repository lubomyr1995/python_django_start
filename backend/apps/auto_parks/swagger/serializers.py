from rest_framework import serializers

from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializerForAutoPark


class SwaggerAutoParkList(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    prev = serializers.CharField()
    next = serializers.CharField()
    page = serializers.IntegerField()
    data = AutoParkSerializer(many=True)


class SwaggerAutoParkCarList(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    prev = serializers.CharField()
    next = serializers.CharField()
    page = serializers.IntegerField()
    data = CarSerializerForAutoPark(many=True)
