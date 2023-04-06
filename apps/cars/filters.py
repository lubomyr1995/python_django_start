from django_filters import rest_framework as filters

from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')

    # class Meta:
    #     model = CarModel
    #     fields = ('brand',)
