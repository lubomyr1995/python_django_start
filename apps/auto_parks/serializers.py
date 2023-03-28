from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel
from ..cars.serializers import CarListSerializer


class AutoParkSerializer(ModelSerializer):
    cars = CarListSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
