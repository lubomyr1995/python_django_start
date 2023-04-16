from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.cars.serializers import CarSerializer
from apps.cars.swagger.serializers import SwaggerCarImageSerializer, SwaggerCarList


def car_list_swagger():
    return method_decorator(
        swagger_auto_schema(
            responses={
                status.HTTP_200_OK: SwaggerCarList()
            }, security=[]),
        'get'
    )


def car_add_images_swagger():
    return method_decorator(
        swagger_auto_schema(
            request_body=SwaggerCarImageSerializer,
            responses={
                status.HTTP_200_OK: CarSerializer()
            }),
        'post'
    )
