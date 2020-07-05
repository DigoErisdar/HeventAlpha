from apps.chars.serializers import CharSerializer
from helper.views import SearchAPIView, ServerFilterMixin


class CharsAPIListView(ServerFilterMixin, SearchAPIView):
    serializer_class = CharSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    search_field = 'nickname'
    user_id_field = 'user_id'
