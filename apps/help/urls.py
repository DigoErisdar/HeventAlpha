from django.urls import path

from apps.help.views import FeedBackAPIView

app_name = 'help'

urlpatterns = [
    path('feedback/', FeedBackAPIView.as_view(), name='feedback'),
]