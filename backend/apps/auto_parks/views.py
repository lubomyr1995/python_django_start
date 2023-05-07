from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auto_parks.swagger import decorators

from ..cars.serializers import CarSerializerForAutoPark
from .filters import AutoParkFilter
from .models import AutoParkModel
from .serializers import AutoParkSerializer


@decorators.auto_park_list_swagger()
class AutoParkListCreateView(ListCreateAPIView):
    """
    get:
        List of auto_parks
    post:
        Create auto_park
    """
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    filterset_class = AutoParkFilter
    # permission_classes = (AllowAny,)
    pagination_class = None

    # def get_queryset(self):
    #     return AutoParkModel.objects.auto_parks_auth(self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@decorators.auto_park_car_list_swagger()
class AutoParkCarListCreateView(ListCreateAPIView):
    """
    get:
        all cars by auto_park id
    post:
        create car by auto_park id
    """
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializerForAutoPark

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = self.serializer_class(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        return auto_park by id
    put:
        full update auto_park by id
    patch:
        partial update auto_park by id
    delete:
        delete auto_park by id
    """
    serializer_class = AutoParkSerializer

    def get_queryset(self):
        return AutoParkModel.objects.filter(user=self.request.user.pk)
