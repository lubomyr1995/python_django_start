from datetime import datetime

from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_car import upload_car_to

from apps.auto_parks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.message)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000000)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    photo = models.ImageField(upload_to=upload_car_to, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
