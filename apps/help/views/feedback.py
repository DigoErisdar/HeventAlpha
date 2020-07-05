from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.help.serializers import FeedBackSerializer


class FeedBackAPIView(CreateAPIView):
    serializer_class = FeedBackSerializer
    permission_classes = [AllowAny]