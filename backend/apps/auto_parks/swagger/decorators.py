from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.auto_parks.swagger.serializers import SwaggerAutoParkCarList, SwaggerAutoParkList


def auto_park_list_swagger():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerAutoParkList()
            }),
        'get'
    )


def auto_park_car_list_swagger():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerAutoParkCarList()
            }),
        'get'
    )
