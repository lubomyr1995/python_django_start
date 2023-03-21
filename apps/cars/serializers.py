from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'number_of_seats', 'type', 'engine_capacity')


class CarSerializerPartial(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year')
