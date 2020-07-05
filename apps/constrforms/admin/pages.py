from django.contrib import admin

from apps.constrforms.models import RequestPage
from apps.guilds.admin import hevent


@admin.register(RequestPage, site=hevent)
class RequestPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'form']
    list_filter = ['form']
    autocomplete_fields = ['form']