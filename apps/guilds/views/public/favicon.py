from django.views.generic import RedirectView
from django_tenants.utils import get_public_schema_name


class FaviconView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = '/static/img/base/favicon.png'
        guild = self.request.tenant
        if guild.schema_name != get_public_schema_name() and guild.profile.favicon:
            url = guild.profile.favicon.url
        return url
