from apps.users.serializers import UserSerializer
from helper.views import SearchAPIView


class UserListAPIView(SearchAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    search_field = 'username'
    vector_fields = ['username']

    def get_serializer_context(self):
        context = super(UserListAPIView, self).get_serializer_context()
        fields = self.model.objects.get_private_fields(self.queryset, self.request)
        context['fields'] = fields
        return context