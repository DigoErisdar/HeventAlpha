from django.contrib import admin
from django.db import connection
from django_tenants.utils import get_public_schema_name

from apps.chars.models import Char, InviteChar
from apps.guilds.admin import hevent
from apps.guilds.models import Guild
from apps.pw.models import Server
from helper.admin import admin_link, PermissionFilterMixin


@admin.register(InviteChar, site=hevent)
class InviteCharAdmin(PermissionFilterMixin, admin.ModelAdmin):

    def get_rase(self, obj):
        return obj.char.rase
    get_rase.short_description = 'Раса'
    get_rase.admin_order_field = 'char__rase'

    list_display = ['char', 'get_rase', 'date_created', 'creator', 'slug']
    list_filter = ['char__rase']
    autocomplete_fields = ['char']

    def get_queryset(self, request):
        qs = super(InviteCharAdmin, self).get_queryset(request)
        if connection.tenant.schema_name != get_public_schema_name():
            qs = qs.filter(char__guild=connection.tenant)
        return qs
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        return super(InviteCharAdmin, self).save_model(request, obj, form, change)