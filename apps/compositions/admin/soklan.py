from django.contrib import admin

from apps.compositions.models import Soklan
from apps.guilds.admin import hevent
from helper.admin import PermissionFilterMixin


@admin.register(Soklan, site=hevent)
class SoklanAdmin(PermissionFilterMixin, admin.ModelAdmin):

    def get_rase(self, obj):
        return obj.char.rase
    get_rase.short_description = 'Раса'
    get_rase.admin_order_field = 'char__rase'

    list_display = ['char', 'get_rase', 'rank', 'composition', 'date_joined']
    list_select_related = ['char', 'rank', 'composition', 'char__rase']
    filter_horizontal = ['permissions']
    list_filter = ['char__rase', 'rank', 'composition']
    date_hierarchy = 'date_joined'
    autocomplete_fields = ['char', 'rank', 'composition']
    fieldsets = (
        ('Персонаж', {
            'fields': (('char', 'composition'), ('rank', 'post'),),
        }),
        ('Права доступа', {
            'classes': ('collapse',),
            'fields': ('is_admin', 'permissions')
        })
    )

    delete_confirmation_template = 'admin/delete_confirmation_soklan.html'
    delete_selected_confirmation_template = 'admin/delete_selected_confirmation_soklan.html'

    def delete_model(self, request, obj):
        obj.delete(comment=request.POST.get('comment', ''))

    def delete_queryset(self, request, queryset):
        queryset.delete(comment=request.POST.get('comment', ''))

