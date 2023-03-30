from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from .models import CarModel
from .serializers import CarSerializer


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
