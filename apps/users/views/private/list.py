from rest_framework.generics import ListAPIView
from apps.users.serializers import PrivateSerializer


class PrivateFieldAPIView(ListAPIView):
    serializer_class = PrivateSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    def get_queryset(self):
        qs = super(PrivateFieldAPIView, self).get_queryset()
        return qs.filter(user=self.request.user)