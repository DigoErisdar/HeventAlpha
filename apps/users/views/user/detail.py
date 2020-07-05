from rest_framework.generics import RetrieveUpdateAPIView
from apps.users.serializers import UserSerializer


class UserDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    def get_serializer_context(self):
        context = super(UserDetailAPIView, self).get_serializer_context()
        fields = self.model.objects.get_private_fields(self.queryset, self.request)
        context['fields'] = fields
        return context
