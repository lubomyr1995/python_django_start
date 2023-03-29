from django.db import models
from django.core import validators as V
from datetime import datetime

from apps.auto_parks.models import AutoParkModel
from core.enums.regex_enum import RegEx


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.message)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000000)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
