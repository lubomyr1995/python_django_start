from rest_framework.views import APIView
from rest_framework.response import Response


class TestApiView(APIView):
    def get(self, *args, **kwargs):
        params_dict = self.request.query_params.dict()
        print(params_dict)
        header_get = self.request.META.get('HTTP_ASD')
        print(header_get)
        return Response('method get')

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response('method post')


class Test2ApiView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        pk = kwargs.get('pk')
        print(pk)
        return Response('ok')
