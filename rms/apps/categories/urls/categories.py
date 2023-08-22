from django.urls import path

from ..views import GetCategoriesView


urlpatterns = [
    path(
        route='',
        view=GetCategoriesView,
        name='get_categories',
    ),
]


