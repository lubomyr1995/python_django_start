from datetime import datetime

from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_car import upload_to

from apps.auto_parks.models import AutoParkModel
from apps.cars.managers import CarManager


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        ordering = ['id']

    brand = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.message)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000000)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CarManager.as_manager()


class CarImageModel(models.Model):
    class Meta:
        db_table = 'cars_images'
        ordering = ['id']

    image = models.ImageField(upload_to=upload_to, blank=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='images')
