from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import UserUpdateSerializer, UserUpdatePasswordSerializer


class CurrentUser(APIView):
    model = User
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user


class CurrentUserAPIView(CurrentUser, RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer


class CurrentUserChangePasswordAPIView(CurrentUser, UpdateAPIView):
    serializer_class = UserUpdatePasswordSerializer
