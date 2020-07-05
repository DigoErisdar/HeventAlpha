from rest_framework.generics import ListAPIView
from apps.constrforms.serializers import FieldSerializer


class FieldListAPIVIew(ListAPIView):
    serializer_class = FieldSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()