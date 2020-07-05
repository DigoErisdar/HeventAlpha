from django.contrib import admin

from apps.constrforms.models.field import TextField, IntegerField, Field, ChoicesForField, ChoiceField, ImageField
from apps.guilds.admin import hevent


@admin.register(Field, site=hevent)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['label', 'help_text', 'required']
    search_fields = ['label']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(TextField, site=hevent)
class TextFieldAdmin(admin.ModelAdmin):
    list_display = ['label', 'help_text', 'required']
    list_filter = ['required']
    search_fields = ['label']


@admin.register(IntegerField, site=hevent)
class IntegerFieldAdmin(admin.ModelAdmin):
    list_display = ['label', 'help_text', 'required', 'min', 'max']
    list_filter = ['required']
    search_fields = ['label']


@admin.register(ChoicesForField, site=hevent)
class ChoicesForField(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(ChoiceField, site=hevent)
class ChoiceFieldAdmin(admin.ModelAdmin):
    list_display = ['label', 'help_text', 'required']
    search_fields = ['label']
    autocomplete_fields = ['choices']


@admin.register(ImageField, site=hevent)
class ImageFieldAdmin(admin.ModelAdmin):
    list_display = ['label', 'help_text', 'required']
    search_fields = ['label']
