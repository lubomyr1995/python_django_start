from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from core.permissions.block_unblock import BlockUnblockUserPermission
from core.permissions.is_superuser import IsSuperuser

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User
from apps.users.swagger import decorators

from .serializers import ProfileSerializer, UserSerializer

UserModel: User = get_user_model()


@decorators.user_list_swagger()
class UserListView(ListAPIView):
    """
    user list without authorization user
    """
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)


@decorators.user_retrieve()
class UserRetrieveDestroyView(RetrieveDestroyAPIView):
    """
    get:
        return user by id
    delete:
        delete user by id
    """
    permission_classes = (IsSuperuser,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)


class UserProfileUpdateView(UpdateAPIView):
    """
    post:
        user profile update
    patch:
        add avatar for user or anything else
    """
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

    # http_method_names = 'patch'

    def get_object(self):
        return self.request.user.profile


@decorators.user_to_admin()
class UserToAdminView(GenericAPIView):
    """
    changed user to admin by user id
    """
    permission_classes = (IsSuperuser,)

    def get_serializer(self, *args, **kwargs):
        pass

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


@decorators.user_to_admin()
class AdminToUserView(GenericAPIView):
    """
    changed admin to user by user id
    """
    permission_classes = (IsSuperuser,)

    def get_serializer(self, *args, **kwargs):
        pass

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


@decorators.user_to_admin()
class UserBlockView(GenericAPIView):
    """
    block user by user id
    """
    permission_classes = (BlockUnblockUserPermission,)

    def get_serializer(self, *args, **kwargs):
        pass

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


@decorators.user_to_admin()
class UserActiveView(GenericAPIView):
    """
    active user by user id
    """
    permission_classes = (BlockUnblockUserPermission,)

    def get_serializer(self, *args, **kwargs):
        pass

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
