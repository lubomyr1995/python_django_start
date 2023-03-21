from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import CarModel
from .serializers import CarSerializer, CarSerializerPartial


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars_qs = CarModel.objects.all()
        serializer = CarSerializerPartial(cars_qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        # if not serializer.is_valid():
        #     return Response('Car not found', status.HTTP_404_NOT_FOUND)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # if not CarModel.objects.filter(pk=pk).exists():
        #     return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
        try:
            car_qs = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car_qs)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        try:
            car_qs = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car_qs, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        try:
            car_qs = CarModel.objects.get(pk=kwargs.get('pk'))
        except CarModel.DoesNotExist:
            return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car_qs, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        try:
            car_qs = CarModel.objects.get(pk=kwargs.get('pk'))
        except CarModel.DoesNotExist:
            return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)

        car_qs.delete()
        return Response({'message': 'created'}, status.HTTP_204_NO_CONTENT)
