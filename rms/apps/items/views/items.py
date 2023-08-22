from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.http import HttpRequest, HttpResponse

from ..core import get_item_core
from ..serializers import (
    ItemModelSerializer,
)


# =============================================GET=============================================


@extend_schema(
    summary='WORKS: User Items',
    description='Returns a list of user items',
    methods=["GET"],
    request=None,
    responses={
        200: OpenApiResponse(response=ItemModelSerializer(many=True))
    },
)
@api_view(['GET'])
def get_items(request: HttpRequest) -> HttpResponse:
    response = get_item_core(request)
    return Response(response.data)
