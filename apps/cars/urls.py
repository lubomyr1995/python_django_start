from django.urls import path

from .views import CarAddImagesView, CarDeleteImageView, CarListView, CarUpdateView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('/<int:pk>', CarUpdateView.as_view(), name='car_update'),
    path('/<int:pk>/add_images', CarAddImagesView.as_view(), name='car_add_images'),
    path('/<int:pk>/delete_image', CarDeleteImageView.as_view(), name='car_delete_image'),
]
