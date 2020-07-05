from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from apps.guilds.admin import hevent
from apps.guilds.views.public.favicon import FaviconView
from apps.users.views.token.obtain import MyTokenObtainPairView

api_token = [
    path('', MyTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]

api_patterns = [

    path('users/', include('apps.users.urls')),
    path('pw/', include('apps.pw.urls')),
    path('token/', include(api_token)),
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
