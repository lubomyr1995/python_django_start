from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from ..cars.serializers import CarListSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkCarListCreateView(CreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarListSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = self.serializer_class(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


# class AutoParkAddCarView(GenericAPIView):
#     queryset = AutoParkModel.objects.all()
#     serializer_class = CarListSerializer
#
#     def get(self, *args, **kwargs):
#         auto_park = self.get_object()
#         serializer = self.serializer_class(auto_park.cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         auto_park = self.get_object()
#         data = self.request.data
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(auto_park=auto_park)
#
#         return Response(serializer.data, status.HTTP_201_CREATED)

class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
