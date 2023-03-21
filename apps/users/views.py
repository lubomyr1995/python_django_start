from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.forms import model_to_dict

from .models import UserModel
from .serializers import UserSerializer


# class UserListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         users = UserModel.objects.all()
#         users = [model_to_dict(i) for i in users]
#         print(users)
#         return Response(users)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         user = UserModel.objects.create(**data)
#         return Response(model_to_dict(user))
#
#
# class UserRetrieveUpdateDestroy(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         try:
#             user = UserModel.objects.get(pk=pk)
#         except UserModel.DoesNotExist:
#             return Response({'error:': 'User not found'}, status.HTTP_400_BAD_REQUEST)
#         return Response(model_to_dict(user))
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data: dict = self.request.data
#
#         try:
#             user = UserModel.objects.get(pk=pk)
#         except UserModel.DoesNotExist:
#             return Response({'error:': 'User not found'}, status.HTTP_400_BAD_REQUEST)
#
#         for k, v in data.items():
#             setattr(user, k, v)
#
#         user.save()
#         return Response(model_to_dict(user))
#
#     def patch(self, *args, **kwargs):
#         pass
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#
#         try:
#             user = UserModel.objects.get(pk=pk)
#         except UserModel.DoesNotExist:
#             return Response('Not Found')
#
#         user.delete()
#         return Response('deleted')

class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        users_qs = UserModel.objects.all()
        serializer = UserSerializer(users_qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        # if not serializer.is_valid():
        #     return Response({'error', str(serializer.errors)})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroy(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            user_qs = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response({'error:': 'User not found'}, status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user_qs)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        try:
            user_qs = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response({'error:': 'User not found'}, status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(instance=user_qs, data=data)
        # serializer = UserSerializer(user_qs, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        try:
            user_qs = UserModel.objects.get(pk=kwargs.get('pk'))
        except UserModel.DoesNotExist:
            return Response({'error:': 'User not found'}, status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user_qs, self.request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response({'error:': 'User not found'}, status.HTTP_400_BAD_REQUEST)

        user.delete()
        return Response('deleted', status.HTTP_204_NO_CONTENT)
