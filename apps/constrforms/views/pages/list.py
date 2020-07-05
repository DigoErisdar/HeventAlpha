from rest_framework.generics import ListAPIView
from apps.constrforms.serializers import PageSerializer


class PageListAPIView(ListAPIView):
    serializer_class = PageSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()