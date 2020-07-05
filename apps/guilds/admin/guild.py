from django.contrib import admin
from django.db import connection
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import get_public_schema_name

from apps.guilds.admin.hevent import hevent
from apps.guilds.admin.inlines import ProfileInline
from apps.guilds.models import Guild


@admin.register(Guild, site=hevent)
class GuildAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'server', 'created_on']
    autocomplete_fields = ['server']
    search_fields = ['name']
    inlines = [ProfileInline]
    exclude = ['schema_name']
    readonly_fields = ['server']

    def get_queryset(self, request):
        qs = super(GuildAdmin, self).get_queryset(request)
        if connection.tenant.schema_name != get_public_schema_name():
            qs = qs.filter(schema_name=connection.tenant.schema_name)
        return qs

    def get_list_filter(self, request):
        fields = []
        if connection.tenant.schema_name == get_public_schema_name():
            fields += ['server']
        return fields

    def has_add_permission(self, request):
        return connection.tenant.schema_name == get_public_schema_name()

    def has_delete_permission(self, request, obj=None):
        return obj and connection.tenant.schema_name == get_public_schema_name()

    def has_change_permission(self, request, obj=None):
        if connection.tenant.schema_name == get_public_schema_name():
            return True
        else:
            return super(GuildAdmin, self).has_change_permission(request, obj)
