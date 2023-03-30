from django.urls import path

from .views import CarListView, CarUpdateView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('/<int:pk>', CarUpdateView.as_view(), name='car_update'),
]
