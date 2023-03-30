from rest_framework.serializers import ModelSerializer

from ..cars.serializers import CarSerializerForAutoPark
from .models import AutoParkModel


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializerForAutoPark(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars', 'user')
        read_only_fields = ('user',)
