from django.contrib import admin

from apps.constrforms.models import RequestStatus
from apps.guilds.admin import hevent
from helper.admin import get_referer


@admin.register(RequestStatus, site=hevent)
class RequestStatusAdmin(admin.ModelAdmin):
    list_display = ['title', 'form']
    list_filter = ['form']
    list_select_related = ['form']
    search_fields = ['title']
    autocomplete_fields = ['form']
    radio_fields = {'action_request': admin.HORIZONTAL, 'action_char': admin.HORIZONTAL, 'color': admin.HORIZONTAL}
    fieldsets = (
        (None, {
            'fields': ('title', 'form', 'color',),
        }),
        ('Действия', {
            'classes': 'collapse',
            'description': 'Действия которые будут срабатывать при смене на данный статус',
            'fields': ('action_request', 'action_char'),
        }),
    )

    def get_queryset(self, request):
        qs = super(RequestStatusAdmin, self).get_queryset(request)
        referer = get_referer(request)
        if referer.isdigit():
            qs = qs.filter(form_id=referer)
        elif referer == 'customform':
            qs = qs.none()
        return qs