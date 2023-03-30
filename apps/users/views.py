from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.permissions.is_superuser import IsSuperuser

from apps.users.models import UserModel as User

from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)


class UserToAdminView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            return Response({'detail': 'already exist is_staff=True'}, status=status.HTTP_400_BAD_REQUEST)
        user.is_staff = True
        user.save()
        serializer = self.serializer_class(user)

        return Response(serializer.data, status.HTTP_200_OK)
