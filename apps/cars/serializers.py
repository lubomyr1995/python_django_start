from abc import ABC

from rest_framework.serializers import ModelSerializer, RelatedField, StringRelatedField, ValidationError

from core.dataclasses.auto_park_dataclass import AutoPark

from .models import CarModel


class CarSerializerForAutoPark(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'photo')


class AutoParkRelatedFieldSerializer(RelatedField, ABC):
    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarSerializer(ModelSerializer):
    # auto_park = StringRelatedField()
    auto_park = AutoParkRelatedFieldSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'photo', 'auto_park')
        # read_only_fields = ('photo',)
        # depth = 2

# def validate(self, attrs):
#     if attrs['year'] == attrs['price']:
#         raise ValidationError({'details': 'year==price'})
#     return attrs
#
#
# def validate_year(self, value):
#     if value == 2001:
#         raise ValidationError('year==2001')
#     return value
