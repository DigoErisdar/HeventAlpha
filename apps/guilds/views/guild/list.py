from django_tenants.utils import get_public_schema_name
from rest_framework.permissions import AllowAny

from apps.guilds.serializers import GuildSerializer
from helper.views import SearchAPIView, ServerFilterMixin


class GuildListAPIView(ServerFilterMixin, SearchAPIView):
    serializer_class = GuildSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.exclude(schema_name=get_public_schema_name()).all()
    permission_classes = [AllowAny]
    search_field = 'name'
    vector_fields = ['name']

    def get_queryset(self):
        qs = super(GuildListAPIView, self).get_queryset()
        current = self.request.GET.get('current', None)
        if current == '1':
            qs = qs.filter(schema_name=self.request.tenant.schema_name)
        return qs


