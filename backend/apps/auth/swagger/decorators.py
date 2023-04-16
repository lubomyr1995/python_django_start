from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .serializers import SwaggerTokenObtainPairAndUserSerializer, SwaggerUserSerializer


def token_obtain_pair_and_user_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerTokenObtainPairAndUserSerializer()
        }, security=[]),
        'post'
    )


def auth_register_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_201_CREATED: SwaggerUserSerializer()
        }, security=[]),
        'post'
    )


def activate_user_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerUserSerializer()
        }, security=[]),
        'get'
    )


def auth_user_info_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: SwaggerUserSerializer()
        }),
        'get'
    )


def recovery_password_request_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: ''
        }, security=[]),
        'post'
    )


def change_password_swagger():
    return method_decorator(
        swagger_auto_schema(responses={
            status.HTTP_200_OK: ''
        }, security=[]),
        'post'
    )
