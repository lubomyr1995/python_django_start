from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AuthRegisterView, AuthUserInfoView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/info', AuthUserInfoView.as_view(), name='auth_user_info'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register')
]
