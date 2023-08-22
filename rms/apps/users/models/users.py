from django.contrib.auth import (
    models as auth_models,
    validators,
)
from django.db import models


class UserModel(auth_models.AbstractUser, auth_models.PermissionsMixin):
    username_validator = validators.UnicodeUsernameValidator()
    username = models.CharField(
        "username",
        max_length=20,
        unique=True,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=50,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = auth_models.UserManager()

    def __str__(self):
        return self.email
