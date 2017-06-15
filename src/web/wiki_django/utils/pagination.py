# -*- coding: utf-8 -*-
import sys

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)


class ProjectDefaultPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CustomPagination(LimitOffsetPagination):
    """
    Pagination with max value for Integer
    """
    default_limit = sys.maxint
