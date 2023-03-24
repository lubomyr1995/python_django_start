from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer, CarListSerializer


class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()

    def get_serializer_class(self):
        return CarSerializer if self.request.method != 'GET' else CarListSerializer

    def get_queryset(self):
        qs = CarModel.objects.all()
        params_dict = self.request.query_params.dict()
        """
        filter year_gte >= зазначеного часу
        """
        if 'year_gte' in params_dict:
            qs = qs.filter(year__gte=params_dict['year_gte'])
        """
            filter year = зазначеному часу
        """
        if 'year' in params_dict:
            qs = qs.filter(year=params_dict['year'])
        return qs

    def perform_create(self, serializer):
        # some logic
        super().perform_create(serializer)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         cars_qs = CarModel.objects.all()
#         serializer = CarSerializerPartial(cars_qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response('Car not found', status.HTTP_404_NOT_FOUND)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)

# class CarRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         car_qs = get_object_or_404(CarModel, pk=pk)
#
#         serializer = CarSerializer(car_qs)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         try:
#             car_qs = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
#         serializer = CarSerializer(car_qs, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         try:
#             car_qs = CarModel.objects.get(pk=kwargs.get('pk'))
#         except CarModel.DoesNotExist:
#             return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
#         serializer = CarSerializer(car_qs, self.request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         try:
#             car_qs = CarModel.objects.get(pk=kwargs.get('pk'))
#         except CarModel.DoesNotExist:
#             return Response({'error': 'Car not found'}, status.HTTP_404_NOT_FOUND)
#
#         car_qs.delete()
#         return Response({'message': 'created'}, status.HTTP_204_NO_CONTENT)

