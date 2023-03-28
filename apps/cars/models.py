from django.db import models
from django.core import validators as v
import datetime

from apps.auto_parks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=50, validators=(v.MaxLengthValidator(40), v.MinLengthValidator(2)))
    year = models.IntegerField(default=1990, validators=(v.MaxValueValidator(datetime.datetime.now().year),))
    price = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
