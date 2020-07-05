from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.db import connection
from django.urls import reverse
from django.utils.html import format_html
from django_tenants.utils import get_public_schema_name


def admin_link(model, empty='-', action='change'):
    """Создаем ссылу для редактирования объекта в админке"""
    if model:
        app = model.__module__.split('.')[-3]
        model_name = model.__class__.__name__.lower()
        link = reverse(f'admin:{app}_{model_name}_{action}', kwargs={'object_id': model.pk})
        return format_html(f'<a href="{link}">{model.__str__()}</a>')
    else:
        return empty


class PublicSortableAdminMixin(admin.ModelAdmin):
    def get_list_display(self, request):
        fields = super().get_list_display(request) or []
        if connection.tenant.schema_name != get_public_schema_name() and '_reorder' in fields:
            fields.remove('_reorder')
        return fields

    def has_add_permission(self, request):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicSortableAdminMixin, self).has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicSortableAdminMixin, self).has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicSortableAdminMixin, self).has_change_permission(request, obj)


class PublicFullHide(admin.ModelAdmin):
    """Запрещает доступ к публичной схеме"""

    def has_module_permission(self, request):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicFullHide, self).has_module_permission(request)

    def has_delete_permission(self, request, obj=None):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicFullHide, self).has_delete_permission(request)

    def has_add_permission(self, request):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicFullHide, self).has_add_permission(request)

    def has_view_or_change_permission(self, request, obj=None):
        if connection.tenant.schema_name != get_public_schema_name():
            return False
        else:
            return super(PublicFullHide, self).has_view_or_change_permission(request)


def _filter_permissions(qs):
    return qs.prefetch_related('content_type') \
        .exclude(content_type__app_label__in=[
        'admin', 'sessions', 'contenttypes', 'easy_thumbnails', 'auth', 'users'
    ])


class PermissionFilterMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in ('permissions',):
            qs = kwargs.get('queryset', db_field.related_model.objects)
            qs = _filter_permissions(qs)
            kwargs['queryset'] = qs
        return super(PermissionFilterMixin, self).formfield_for_manytomany(db_field, request, **kwargs)


def get_referer(request):
    link = request.META['HTTP_REFERER']
    return link.split('/')[-3]


class DontLog:
    def log_change(self, request, object, message):
        return False

    def log_addition(self, request, object, message):
        return False

    def log_deletion(self, request, object, object_repr):
        return False
