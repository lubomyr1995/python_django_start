from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    ActivateUserView,
    AuthRegisterView,
    AuthUserInfoView,
    ChangePasswordView,
    RecoveryPasswordRequestView,
    SocketTokenView,
    TokenObtainPairAndUserView,
)

urlpatterns = [
    path('', TokenObtainPairAndUserView.as_view(), name='auth_login'),
    path('/info', AuthUserInfoView.as_view(), name='auth_user_info'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='activate_user'),
    path('/recovery_password', RecoveryPasswordRequestView.as_view(), name='recovery_password'),
    path('/recovery_password/<str:token>', ChangePasswordView.as_view(), name='change_password'),
    path('/socket', SocketTokenView.as_view(), name='auth_get_socket_token')
]
