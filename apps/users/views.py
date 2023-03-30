from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions.is_superuser import IsSuperuser

from apps.users.models import UserModel as User

from .serializers import AddAvatarSerializer, UserSerializer

UserModel: User = get_user_model()


class UserListView(APIView):
    def get(self, *args, **kwargs):
        serializer = UserSerializer(UserModel.objects.all(), many=True)
        print('*********')
        print(serializer.data)
        print('*********')
        return Response(serializer.data, status.HTTP_200_OK)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserAddAvatarView(UpdateAPIView):
    http_method_names = ('patch',)
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile


class UserToAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            return Response({'details': 'already exist is_staff=True'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = True
        user.save()
        serializer = self.serializer_class(user)

        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            return Response({'details': 'already exist is_staff=False'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = False
        user.save()
        serializer = self.serializer_class(user)

        return Response(serializer.data, status.HTTP_200_OK)


class UserIsActiveForAdminsView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            return Response({'details': 'already exist is_active=True'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = True
        user.save()
        serializer = self.serializer_class(user)

        return Response(serializer.data, status.HTTP_200_OK)


class UserIsDeactivateForAdminsView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            return Response({'details': 'already exist is_active=False'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save()
        serializer = self.serializer_class(user)

        return Response(serializer.data, status.HTTP_200_OK)
