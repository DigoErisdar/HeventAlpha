from helper.views import SearchAPIView
from apps.compositions.serializers import CompositionSerializer


class CompositionListAPIView(SearchAPIView):
    serializer_class = CompositionSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    # TODO: add permissions
