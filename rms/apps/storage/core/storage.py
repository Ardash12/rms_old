from typing import List

from rest_framework.parsers import JSONParser

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpRequest

from ..models import StorageModel

from ..serializers import (
    StorageCreationRequestSerializer,
    StorageModelSerializer,
)


# =============================================GET=============================================

def get_storage_core(request: HttpRequest) -> List[StorageModel]:
    """Returns a list of BoardColumnModel objects that belong to the request.users

    Parameters:
    - request (HttpRequest): A Django HttpRequest object.

    Returns:
    - List[StorageModel]: A list of StorageModel objects sorted by the name field, serialized using the StorageModelSerializer class.

    """
    
    user = request.user
    storage = StorageModel.objects.filter(user=user).order_by("name")
    return StorageModelSerializer(storage, many=True)


# =============================================POST============================================

def create_storage_core(request: HttpRequest) -> List[StorageModel]:
    """Create a new storage.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - bool: True if the column was created successfully, False otherwise.

    Raises:
    - ValidationError: If the data provided in the request is not valid.
    """
        
    data = JSONParser().parse(request)
    serializer = StorageCreationRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data["user"] = request.user
    serializer.save()
    
    
    