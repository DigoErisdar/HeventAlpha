from django.urls import path, include
from .views import *


app_name = 'compositions'

rank_urls = [
    path('', RankListAPIView.as_view(), name='rank-list'),
]

soklan_urls = [
    path('', SoklanListAPIView.as_view(), name='soklan-list'),
]

urlpatterns = [
    path('', CompositionListAPIView.as_view(), name="list"),
    path('ranks/', include(rank_urls)),
    path('soklans/', include(soklan_urls)),
]