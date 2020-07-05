from django.urls import path
from apps.pw.views import *

app_name = 'pw'

urlpatterns = [
    path('servers/', ServerListAPIView.as_view(), name='servers'),
    path('rases/', RaseListAPIView.as_view(), name='rases')
]