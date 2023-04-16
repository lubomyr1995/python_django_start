from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from apps.cars.swagger import decorators

from .filters import CarFilter
from .models import CarImageModel, CarModel
from .serializers import CarImageSerializer, CarSerializer


@decorators.car_list_swagger()
class CarListView(ListAPIView):
    """
    List of cars
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)
    filterset_class = CarFilter
    filterset_fields = ('brand',)


class CarUpdateView(UpdateAPIView):
    """
    put:
        full update car by id
    patch:
        partial update car by id
    """
    http_method_names = ['put', 'patch']
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


@decorators.car_add_images_swagger()
class CarAddImagesView(GenericAPIView):
    """
        Add images for car by id
    """
    queryset = CarModel.objects.all()
    serializer_class = CarImageSerializer

    # @swagger_auto_schema(responses={status.HTTP_200_OK: CarSerializer()})
    def post(self, *args, **kwargs):
        car = self.get_object()
        files = self.request.FILES
        for key in files:
            serializer = self.serializer_class(data={'image': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)


class CarDeleteImageView(DestroyAPIView):
    """
        delete car image by id
    """
    queryset = CarImageModel.objects.all()

    def perform_destroy(self, instance):
        instance.image.delete()
        instance.delete()
