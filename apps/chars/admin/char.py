from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.db import connection
from django_tenants.utils import get_public_schema_name

from apps.chars.models import Char
from apps.guilds.admin import hevent
from apps.pw.models import Server
from helper.admin import admin_link, PermissionFilterMixin, get_referer, DontLog


@admin.register(Char, site=hevent)
class CharAdmin(DontLog, PermissionFilterMixin, admin.ModelAdmin):
    search_fields = ['nickname']
    related = ['user', 'guild', 'rase', 'server']
    list_select_related = related
    autocomplete_fields = related

    def rase_link(self, obj):
        return admin_link(obj.rase, 'Нет расы')

    rase_link.short_description = 'Раса'
    rase_link.admin_order_field = 'rase'

    def server_link(self, obj):
        return admin_link(obj.server, 'Нет сервера')

    server_link.short_description = 'Сервер'
    server_link.admin_order_field = 'server'

    def guild_link(self, obj):
        return admin_link(obj.guild, 'Нет гильдии')

    guild_link.short_description = 'Гильдия'
    guild_link.admin_order_field = 'guild'

    def user_link(self, obj):
        return admin_link(obj.user, 'Нет владельца')

    user_link.short_description = 'Владелец'
    user_link.admin_order_field = 'user'

    def get_queryset(self, request):
        qs = super(CharAdmin, self).get_queryset(request)
        referer = get_referer(request)
        if referer == 'invitechar':
            qs = qs.filter(user__isnull=True)
        elif referer == 'soklan':
            qs = qs.filter(soklan__isnull=True)
        elif referer == 'request':
            qs = qs.filter(soklan__isnull=True, user__isnull=False)
        if referer not in ['request'] and connection.tenant.schema_name != get_public_schema_name():
            qs = qs.filter(guild=connection.tenant)
        return qs

    def get_list_filter(self, request):
        list_filter = ['rase']
        if connection.tenant.schema_name == get_public_schema_name():
            list_filter += ['server', 'guild']
        return list_filter

    def get_list_display(self, request):
        list_display = ['nickname', 'rase_link', 'user_link']
        if connection.tenant.schema_name == get_public_schema_name():
            list_display += ['server_link', 'guild_link']
        return list_display

    def get_readonly_fields(self, request, obj=None):
        fields = []
        if connection.tenant.schema_name != get_public_schema_name():
            fields += ['user', 'server', 'guild']
        return fields

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user is None:
            return super(CharAdmin, self).has_delete_permission(request, obj)
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user is None:
            return super(CharAdmin, self).has_change_permission(request, obj)
        else:
            return False

    def save_model(self, request, obj, form, change):
        if not change and connection.tenant.schema_name != get_public_schema_name():
            obj.guild = connection.tenant
        return super(CharAdmin, self).save_model(request, obj, form, change)

    def get_changeform_initial_data(self, request):
        initial = super(CharAdmin, self).get_changeform_initial_data(request) or {}
        if connection.tenant.schema_name != get_public_schema_name():
            initial['server'] = Server.objects.get(guild__schema_name=connection.tenant.schema_name)
        return initial
