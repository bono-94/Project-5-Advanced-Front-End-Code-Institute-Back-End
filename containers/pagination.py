from rest_framework.pagination import BasePagination

class NoPagination(BasePagination):
    def paginate_queryset(self, queryset, request, view=None):
        return None

    def get_paginated_response(self, data):
        return data