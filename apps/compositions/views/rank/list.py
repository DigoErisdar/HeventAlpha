from helper.views import SearchAPIView
from apps.compositions.serializers import RankSerializer


class RankListAPIView(SearchAPIView):
    serializer_class = RankSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    # TODO: Add permissions
    search_field = 'title'
