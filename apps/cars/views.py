from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer

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


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
