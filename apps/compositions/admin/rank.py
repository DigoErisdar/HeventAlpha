from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from apps.compositions.models import Rank
from apps.guilds.admin import hevent
from helper.admin import PermissionFilterMixin


@admin.register(Rank, site=hevent)
class RankAdmin(PermissionFilterMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    filter_horizontal = ['permissions']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
