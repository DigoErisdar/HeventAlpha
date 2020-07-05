from rest_framework.permissions import AllowAny

from apps.pw.serializers import RaseSerializer
from helper.views import SearchAPIView


class RaseListAPIView(SearchAPIView):
    serializer_class = RaseSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    vector_fields = ['title']
    search_field = 'title'

    permission_classes = [AllowAny]