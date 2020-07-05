from django.urls import path, include

from apps.constrforms.views import RequestsListAPIView, RequestApiView

app_name = 'api-requests'

page_urls = [
    path('', RequestsListAPIView.as_view(), name='page'),
]

urlpatterns = [
    path('request/<str:slug>.<pk>/', RequestApiView.as_view(), name='request'),
    path('<str:slug>.<pk>/', include(page_urls)),
]