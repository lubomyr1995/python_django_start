from django.urls import path

from .views import AutoParkListCreateView, AutoParkCarListCreateView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy'),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view(), name='auto_park_car_list_create')
]
