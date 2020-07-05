from django.urls import path, include

from apps.constrforms.views import PageListAPIView, FieldListAPIVIew, PageDetailAPIView

app_name = 'requests'

field_urls = [
    path('', FieldListAPIVIew.as_view(), name='field-list'),
]

urlpatterns = [
    path('', PageListAPIView.as_view(), name='list'),
    path('fields/', include(field_urls)),
    path('<pk>/', PageDetailAPIView.as_view(), name='detail'),
]
