from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from core.permissions.block_unblock import BlockUnblockUserPermission
from core.permissions.is_superuser import IsSuperuser

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

from .serializers import ProfileSerializer, UserSerializer

UserModel: User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperuser,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)


class UserProfileUpdateView(UpdateAPIView):
    http_method_names = 'patch'
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            return Response({'detail': 'already exist is_staff=True'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = True
        user.save()
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            return Response({'detail': 'already exist is_staff=False'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserBlockView(GenericAPIView):
    permission_classes = (BlockUnblockUserPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserActiveView(GenericAPIView):
    permission_classes = (BlockUnblockUserPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
