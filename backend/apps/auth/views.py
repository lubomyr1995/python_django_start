from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

from apps.auth.serializers import EmailSerializer, PasswordSerializer, TokenObtainPairAndUserSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from .swagger import decorators

UserModel: User = get_user_model()


@decorators.token_obtain_pair_and_user_swagger()
class TokenObtainPairAndUserView(TokenObtainPairView):
    """
    Login
    """
    serializer_class = TokenObtainPairAndUserSerializer


@decorators.auth_register_swagger()
class AuthRegisterView(CreateAPIView):
    """
    Registration user
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@decorators.auth_user_info_swagger()
class AuthUserInfoView(RetrieveAPIView):
    """
    Return authorization user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@decorators.activate_user_swagger()
class ActivateUserView(GenericAPIView):
    """
    Activate User by token
    """
    permission_classes = (AllowAny,)

    @staticmethod
    def get(*args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


@decorators.recovery_password_request_swagger()
class RecoveryPasswordRequestView(GenericAPIView):
    """
    Request for password recovery
    """
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, *args, **kwargs):
        email = self.request.data
        serializer = self.serializer_class(data=email)
        serializer.is_valid(raise_exception=True)
        user_email = serializer.data.get('email')
        user = get_object_or_404(UserModel, email=user_email)
        EmailService.recovery_password(user)
        return Response(status=status.HTTP_200_OK)


@decorators.change_password_swagger()
class ChangePasswordView(GenericAPIView):
    """
    set password for recovered user
    """
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    @atomic
    def post(self, *args, **kwargs):
        token = kwargs.get('token')
        new_password = self.request.data
        user: User = JWTService.validate_token(token, RecoveryToken)
        serializer = self.serializer_class(data=new_password)
        serializer.is_valid(raise_exception=True)
        # user.set_password(serializer.data.get('password'))
        user.set_password(new_password['password'])
        user.save()
        return Response(status=status.HTTP_200_OK)
