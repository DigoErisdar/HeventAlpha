from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from apps.guilds.admin import hevent
from apps.guilds.views.public.favicon import FaviconView

api_patterns = [

    path('chars/', include('apps.chars.urls')),
    path('guilds/', include('apps.guilds.urls')),
    path('compositions/', include('apps.compositions.urls')),
    path('requests/', include('apps.constrforms.urls')),

    path('help/', include('apps.help.urls')),
]


urlpatterns = [
    path('admin/', hevent.urls),
    path('favicon.ico', FaviconView.as_view(), name='favicon'),
    path('api/', include(api_patterns))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
