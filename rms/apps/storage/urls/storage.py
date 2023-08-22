from django.urls import path

from ..views import create_storage, get_storage


urlpatterns = [
    path(
        route='',
        view=get_storage,
        name='get_storage',
    ),
    path(
        route='add/',
        view=create_storage,
        name='create_storage',
    ),
]


