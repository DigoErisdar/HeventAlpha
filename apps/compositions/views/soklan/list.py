from helper.views import SearchAPIView
from apps.compositions.serializers import SoklanSerializer


class SoklanListAPIView(SearchAPIView):
    serializer_class = SoklanSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    search_field = 'char__nickname'
    user_id_field = 'char__user_id'
