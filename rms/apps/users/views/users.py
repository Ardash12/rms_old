from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import AllowAny

from django.http import HttpResponse, HttpRequest

from ..core import sign_in_core

from ..serializers import (
    UserRegistrationRequestSerializer,
)

from ..services import (
    GetTokenHttpResponseService,
    GetLogoutHttpResponse,
)


# =============================================POST=============================================




@extend_schema(
    description="WORKS: Take user's email and password and return 'access' and 'refresh' tokens in cookies",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return GetTokenHttpResponseService(user)

