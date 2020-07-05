from django.contrib import admin
from django.utils.html import format_html

from apps.constrforms.models import Claim
from apps.guilds.admin import hevent


@admin.register(Claim, site=hevent)
class RequestAdmin(admin.ModelAdmin):

    def get_rase(self, obj):
        return obj.char.rase
    get_rase.short_description = 'Раса'
    get_rase.admin_oreder_field = 'char__rase'

    def get_text(self):
        return format_html(self.text)
    get_text.short_description = 'Текст'

    list_display = ['char', 'get_rase', 'date_created', 'status', 'form']
    list_select_related = ['char', 'char__rase', 'form']
    list_filter = ['status', 'char__rase', 'form']
    readonly_fields = [get_text]
    date_hierarchy = 'date_created'
    autocomplete_fields = ['char', 'form']
