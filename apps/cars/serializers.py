from rest_framework.serializers import ModelSerializer

from .models import CarModel


class CarSerializerForAutoPark(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price')


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'auto_park')
