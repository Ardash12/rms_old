from django.urls import path

from ..views import GetItemsView


urlpatterns = [
    path(
        route='',
        view=GetItemsView,
        name='get_items',
    ),
]


