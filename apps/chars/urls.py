from django.urls import path

from apps.chars.views import CharsAPIListView

app_name = 'chars'

urlpatterns = [
    path('', CharsAPIListView.as_view(), name='list'),
]