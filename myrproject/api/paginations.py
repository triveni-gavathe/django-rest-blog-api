from rest_framework.pagination import PageNumberPagination,CursorPagination,LimitOffsetPagination
from rest_framework.response import Response

class custompagination(PageNumberPagination):
    page_size_query_param='page_size'
    page_query_param='page-num'
    max_page_size=5
    def get_paginated_response(self, data):
        return Response({
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'count':self.page.paginator.count,
            'page_size':self.page_size,
            'result':data
        })
class Mycursorpaginatation(CursorPagination):
    page_size=5
    ordering='id'
    
class Mylimitoffset(LimitOffsetPagination):
    default_limit=5
    max_limit=20        