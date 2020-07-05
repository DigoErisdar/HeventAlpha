from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from apps.guilds.admin import hevent
from apps.pw.models import Server
from helper.admin import PublicSortableAdminMixin


@admin.register(Server, site=hevent)
class ServerAdmin(PublicSortableAdminMixin, SortableAdminMixin, TenantAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
