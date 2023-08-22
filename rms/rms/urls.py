from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('obj_card.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/', 
        SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/', 
        SpectacularRedocView.as_view(url_name='schema'), 
        name='redoc',
    ),
    path(
        'categoris/',
        include('apps.categories.urls.categories'),
        name='categories',
    ), 
    path(
        'items/',
        include('apps.items.urls.items'),
        name='items',
    ), 
    path(
        'storage/',
        include('apps.storage.urls.storage'),
        name='items',
    ), 
    path(
        'users/',
        include('apps.users.urls.users'),
        name='items',
    ), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("schema/",
                  SpectacularAPIView.as_view(),
                  name="schema"
            ),
            path(
                "docs/",
                SpectacularSwaggerView.as_view(
                    template_name="swagger-ui.html",
                    url_name="schema",
                ),
                name="swagger-ui",
            ),
        ]
    )
