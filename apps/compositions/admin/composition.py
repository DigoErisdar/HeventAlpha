from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from apps.compositions.forms import CompositionAdminForm
from apps.compositions.models import Composition
from apps.guilds.admin import hevent


@admin.register(Composition, site=hevent)
class CompositionAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = CompositionAdminForm
    list_display = ['title']
    search_fields = ['title']
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('КХ настройки', {
            'classes': ('collapse',),
            'fields': ('close_loot', 'user_attempts',)
        })
    )
