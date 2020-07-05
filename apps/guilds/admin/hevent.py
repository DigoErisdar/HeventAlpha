from django.conf import settings
from django.contrib import admin
from django.db import connection
from django_tenants.utils import get_public_schema_name

from apps.compositions.models import Soklan
from apps.guilds.forms.admin_login import HeventUserAuthenticationForm


class HeventAdminSite(admin.AdminSite):
    def has_permission(self, request):
        visitor = request.user
        return visitor.is_authenticated and visitor.is_global_admin \
                or connection.tenant.schema_name != get_public_schema_name() \
               and Soklan.objects.filter(is_admin=True, char__user_id=visitor.id).exists()

    site_header = f'{settings.SITE_NAME} Админ-панель'
    site_title = settings.SITE_NAME
    login_form = HeventUserAuthenticationForm


hevent = HeventAdminSite()
