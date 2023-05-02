from rest_framework.views import APIView, Request, Response
from rest_framework.pagination import PageNumberPagination
from .base_views import (
    DestroyBaseView,
    ListBaseView,
    CreateBaseView,
    RetrieveBaseView,
    UpdateBaseView,
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10


class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None
    url_params_name = "pk"
    pagination_class = "rest_framework.pagination.PageNumberPagination"


class ListGenericView(ListBaseView, GenericBaseView):
    def get(self, request: Request) -> Response:
        return super().list(request)


class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request: Request) -> Response:
        return super().create(request)


class RetrieveGenericView(RetrieveBaseView, GenericBaseView):
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().retrieve(request, *args, **kwargs)


class UpdateGenericView(UpdateBaseView, GenericBaseView):
    def patch(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().update(request, *args, **kwargs)


class DestroyGenericView(DestroyBaseView, GenericBaseView):
    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().destroy(request, *args, **kwargs)
