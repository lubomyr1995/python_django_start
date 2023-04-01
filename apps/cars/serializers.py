from abc import ABC

from rest_framework.serializers import ModelSerializer, RelatedField, StringRelatedField, ValidationError

from core.dataclasses.auto_park_dataclass import AutoPark

from .models import CarImageModel, CarModel


class CarImageSerializer(ModelSerializer):
    class Meta:
        model = CarImageModel
        fields = ('image',)

    def to_representation(self, instance):
        return instance.image.url


class CarSerializerForAutoPark(ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'images')


class AutoParkRelatedFieldSerializer(RelatedField, ABC):
    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarSerializer(ModelSerializer):
    auto_park = AutoParkRelatedFieldSerializer(read_only=True)
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'images', 'auto_park')
