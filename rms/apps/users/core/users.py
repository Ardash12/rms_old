import requests

from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpRequest

from ..models import UserModel

from ..services import UserManagerService


@transaction.atomic
def sign_in_core(request: HttpRequest) -> UserModel:
    """
    Sign in a user, given their email and password.

    Args:
        request (django.http.HttpRequest): The HTTP request object.

    Returns:
        UserModel: Present in database user object.
    """

    data = JSONParser().parse(request)
    email = data['email']
    password = data['password']
    try:
        user = UserModel.objects.get(email=email)
        if not user.check_password(password):
            raise AuthenticationFailed()
    except UserModel.DoesNotExist:
        raise AuthenticationFailed()
    return user