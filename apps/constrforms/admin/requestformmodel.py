from django.contrib import admin

from apps.constrforms.models import CustomForm, FormField
from apps.guilds.admin import hevent
from adminsortable2.admin import SortableInlineAdminMixin


class FormFieldInline(SortableInlineAdminMixin, admin.TabularInline):
    model = FormField
    min_num = 1
    extra = 1
    autocomplete_fields = ['field']
    verbose_name = "Поле"
    verbose_name_plural = 'Поля'
    classes = ['collapse']


@admin.register(CustomForm, site=hevent)
class CustomFormAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [FormFieldInline]
    autocomplete_fields = ['default_status']
