from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ..cars.serializers import CarSerializerForAutoPark
from .filters import AutoParkFilter
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):

    serializer_class = AutoParkSerializer
    filterset_class = AutoParkFilter

    def get_queryset(self):
        return AutoParkModel.objects.auto_parks_auth(self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoParkCarListCreateView(ListCreateAPIView):
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
    serializer_class = AutoParkSerializer

    def get_queryset(self):
        return AutoParkModel.objects.filter(user=self.request.user.pk)
