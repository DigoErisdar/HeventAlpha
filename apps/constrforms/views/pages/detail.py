from rest_framework.generics import RetrieveAPIView
from apps.constrforms.serializers import PageSerializer


class PageDetailAPIView(RetrieveAPIView):
    serializer_class = PageSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
