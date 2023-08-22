from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import CategoryModel

from ..serializers import (
    CategoryModelSerializer,
    CategoryResponseSerializer,
)


# =============================================GET=============================================

def get_category_core(request: HttpRequest) -> List[CategoryModel]:
    categories = CategoryModel.objects.all()
    return CategoryModelSerializer(categories, many=True)
