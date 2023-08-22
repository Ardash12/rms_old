from typing import Any

from django.apps import apps
from django.contrib.auth import (
    hashers,
    models,
    password_validation,
)


class UserManager(models.UserManager):
    """
    A class that provides a custom user manager to create users and superusers.

    Methods
    -------
    _create_user(email: str, username: Optional[str], password: Optional[str], **extra_fields: Any) -> UserModel:
        Creates a new UserModel instance given the email, username, password and any additional fields.

    create_user(email: str, username: str, password: Optional[str] = None, **extra_fields: Any) -> UserModel:
        Creates a regular user instance by calling '_create_user()' method with is_superuser flag set to False.

    create_superuser(username: str, password: Optional[str] = None, **extra_fields: Any) -> UserModel:
        Creates a superuser instance by calling '_create_user()' method with is_superuser flag set to True.

    Raises
    ------
    ValueError:
        If email is not provided for '_create_user()' method
        If is_superuser flag is not set to True for a superuser instance
    """

    def _create_user(self, email: str, username: str, password: str, **extra_fields: Any):
        """
        Creates a new UserModel instance given the email, username, password and any additional fields.

        Parameters
        ----------
        email : str
            Email of the user to be created
        username : str
            Username of the user to be created
        password : str
            Password of the user to be created
        **extra_fields : Any
            Any additional fields to be added to the user model instance

        Returns
        -------
        user : UserModel
            UserModel instance representing the created user

        Raises
        ------
        ValueError:
            If email is not provided
        """

        if not email:
            raise ValueError("The given email must be set")
        GlobalUserModel = apps.get_model('users', 'UserModel')
        GlobalUserModel.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        password_validation.validate_password(password)
        user.password = hashers.make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, username: str, password: str=None, **extra_fields: Any):
        """
        Creates a new user with the given email, username, and password (defaulting to None).

        Parameters
        ----------
        email : str
            Email of the user to be created
        username : str
            Username of the user to be created
        password : str, optional
            Password of the user to be created, defaults to None
        **extra_fields : Any
            Any additional fields to be added to the user model instance

        Returns
        -------
        user : UserModel
            UserModel instance representing the created user

        Raises
        ------
        ValueError:
            If email is not provided
        """


        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email=email, username=username, password=password, **extra_fields)

    def create_superuser(self, username: str, password: str=None, **extra_fields: Any):
        """
        Create a superuser with the given username and password.

        :param username: The username for the superuser, a string.
        :param password: The password for the superuser, a string. Default: None.
        :param **extra_fields: Optional additional fields to be included for the superuser.
        :return: The created user object.
        :raises ValueError: If the is_superuser field is not True for the superuser.

        This method creates a superuser with the given username and password, as well as any
        additional fields provided as keyword arguments. The is_superuser field is set to True
        for the superuser, and if this field is not explicitly set to True in the extra_fields
        parameter, it will be set to True automatically.
        """

        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username=username, password=password, **extra_fields)