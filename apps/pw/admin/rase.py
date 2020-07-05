from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from apps.guilds.admin import hevent
from apps.pw.models import Rase
from helper.admin import PublicSortableAdminMixin


@admin.register(Rase, site=hevent)
class RaseAdmin(PublicSortableAdminMixin, SortableAdminMixin, TenantAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'get_ico']
    search_fields = ['title']