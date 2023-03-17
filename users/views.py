from rest_framework.response import Response
from rest_framework.views import APIView

from .services import UserService


class UserAPIView(APIView, UserService):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._read_file()


def something_go_wrong(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            return Response({'error': str(err)})

    return inner


class UserListCreateView(UserAPIView):
    def get(self, *args, **kwargs):
        return Response(self.get_all())

    @something_go_wrong
    def post(self, *args, **kwargs):
        data = self.request.data
        return Response(self.add(data))


class UserRetrieveUpdateDestroyView(UserAPIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        return Response(self.get_by_id(pk))

    @something_go_wrong
    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        user = self.update_by_id_all(pk, data)
        return Response(user)

    def patch(self, *args, **kwargs):
        return Response(self.update_by_id_partial(kwargs.get('pk'), self.request.data))

    def delete(self, *args, **kwargs):
        return Response(self.delete_by_id(kwargs.get('pk')))
