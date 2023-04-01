from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import CarImageModel, CarModel
from .serializers import CarImageSerializer, CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        qs = CarModel.objects.all()
        params_dict = self.request.query_params.dict()

        if 'year' in params_dict:
            qs = qs.filter(year__gte=params_dict['year'])

        return qs


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
