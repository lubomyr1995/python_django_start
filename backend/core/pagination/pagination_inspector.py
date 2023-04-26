from collections import OrderedDict

from rest_framework.pagination import CursorPagination, LimitOffsetPagination, PageNumberPagination

from drf_yasg import openapi
from drf_yasg.inspectors import DjangoRestResponsePagination


class PaginationInspector(DjangoRestResponsePagination):

    def get_paginated_response(self, paginator, response_schema):
        assert response_schema.type == openapi.TYPE_ARRAY, "array return expected for paged response"
        paged_schema = None
        if isinstance(paginator, (LimitOffsetPagination, PageNumberPagination, CursorPagination)):
            has_count = not isinstance(paginator, CursorPagination)
            paged_schema = openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=OrderedDict((
                    ('total_items', openapi.Schema(type=openapi.TYPE_INTEGER) if has_count else None),
                    ('total_pages', openapi.Schema(type=openapi.TYPE_INTEGER) if has_count else None),
                    ('prev', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('next', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('page', openapi.Schema(type=openapi.TYPE_INTEGER) if has_count else None),

                    ('data', response_schema),
                )),
                required=['results']
            )

            if has_count:
                paged_schema.required.insert(0, 'count')

        return paged_schema
