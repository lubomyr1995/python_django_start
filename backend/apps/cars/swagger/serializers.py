from rest_framework import serializers

from apps.cars.serializers import CarSerializer


class SwaggerCarImageSerializer(serializers.Serializer):
    image = serializers.ImageField()


class SwaggerCarList(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    prev = serializers.CharField()
    next = serializers.CharField()
    page = serializers.IntegerField()
    data = CarSerializer(many=True)
