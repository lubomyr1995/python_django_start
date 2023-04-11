import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'
    max_page_size = 20

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.get_page_size(self.request))
        _prev = self.page.previous_page_number() if self.get_previous_link() else None
        _next = self.page.next_page_number() if self.get_next_link() else None
        return Response({
            'total_items': count,
            'total_pages': total_pages,
            'prev': _prev,
            'next': _next,
            'page': self.page.number,
            'data': data
        })
