from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class AuthUserInfoView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(*args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class RecoveryPasswordRequestView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = self.request.data
        serializer = EmailSerializer(data=email)
        serializer.is_valid(raise_exception=True)
        user_email = serializer.data.get('email')
        user = get_object_or_404(UserModel, email=user_email)
        EmailService.recovery_password(user)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs.get('token')
        new_password = self.request.data
        user = JWTService.validate_token(token, RecoveryToken)
        serializer = PasswordSerializer(data=new_password)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data.get('password'))
        user.save()
        return Response({'details': 'Your password changed'}, status.HTTP_200_OK)
