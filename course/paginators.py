from rest_framework.pagination import PageNumberPagination


class StagePagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class SubjectPagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
