from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=50)
    year = models.IntegerField()
    number_of_seats = models.IntegerField()
    type = models.CharField(max_length=100)
    engine_capacity = models.FloatField()

