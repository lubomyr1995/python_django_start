from django.db import models
from django.core import validators as v
import datetime


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=50, null=True, validators=(v.MaxLengthValidator(40), v.MinLengthValidator(2)))
    year = models.IntegerField(default=1990, validators=(v.MaxValueValidator(datetime.datetime.now().year),))
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __repr__(self):
    #     return str(self.__dict__)
