from django.urls import path, include

from apps.users.views import UserListAPIView, UsersRegisterAPIView, PrivateFieldAPIView, CurrentUserAPIView, \
    UserDetailAPIView, CurrentUserChangePasswordAPIView

app_name = 'users'

current_urls = [
    path('', CurrentUserAPIView.as_view(), name='current'),
    path('change_password/', CurrentUserChangePasswordAPIView.as_view(), name='change-password'),
]


urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('register/', UsersRegisterAPIView.as_view(), name='register'),
    path('privates/', PrivateFieldAPIView.as_view(), name='privates'),
    path('current/', include(current_urls)),
    path('<pk>/', UserDetailAPIView.as_view(), name='detail'),
]
