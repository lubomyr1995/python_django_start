from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.pagination.page_pagination import PagePagination

from .filters import CarFilter
from .models import CarImageModel, CarModel
from .serializers import CarImageSerializer, CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    # queryset = CarModel.objects.cars_by_auto_park_id(2)
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)
    filterset_class = CarFilter
    filterset_fields = ('brand',)
# class CarListView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     pagination_class = PagePagination
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         queryset = CarModel.objects.all()
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


class CarUpdateView(UpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddImagesView(GenericAPIView):
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        car = self.get_object()
        files = self.request.FILES
        for key in files:
            serializer = CarImageSerializer(data={'image': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)


class CarDeleteImageView(DestroyAPIView):
    queryset = CarImageModel.objects.all()

    def perform_destroy(self, instance):
        instance.image.delete()
        instance.delete()
