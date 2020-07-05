from rest_framework.permissions import AllowAny

from apps.pw.serializers import ServerSerializer
from helper.views import SearchAPIView


class ServerListAPIView(SearchAPIView):
    serializer_class = ServerSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    search_field = 'title'
    permission_classes = [AllowAny]
