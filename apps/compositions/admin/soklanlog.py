from django.contrib import admin

from apps.compositions.models import SoklanLog
from apps.guilds.admin import hevent


@admin.register(SoklanLog, site=hevent)
class SoklanLogAdmin(admin.ModelAdmin):

    def get_rase(self, obj):
        return obj.char.rase

    get_rase.short_description = "Раса"
    get_rase.admin_order_field = 'char__rase'

    list_display = ['char', 'get_rase', 'action', 'date_created', 'comment']
    list_filter = ['action', 'char__rase']
    list_select_related = ['char', 'char__rase']

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
