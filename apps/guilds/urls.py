from django.urls import path

from apps.guilds.views import GuildListAPIView

app_name = 'guilds'

urlpatterns = [
    path('', GuildListAPIView.as_view(), name='list'),
]