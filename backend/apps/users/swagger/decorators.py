from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.auth.swagger.serializers import SwaggerUserSerializer
from apps.users.swagger.serializers import SwaggerUserList


def user_list_swagger():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerUserList()
            }
        ),
        'get'
    )


def user_retrieve():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerUserSerializer()
            }),
        'get'
    )


def user_to_admin():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerUserSerializer()
            }),
        'patch'
    )


def user_partial_update():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerUserSerializer()
            }),
        'patch'
    )
