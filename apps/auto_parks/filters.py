from django_filters import rest_framework as filters

from apps.auto_parks.models import AutoParkModel


class AutoParkFilter(filters.FilterSet):
    cars_year_lt = filters.CharFilter('cars', 'year__lt', distinct=True)
    cars_year_gt = filters.CharFilter('cars', 'year__gt', distinct=True)
