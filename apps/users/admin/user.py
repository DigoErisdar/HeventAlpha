from django.contrib import admin
from django.db import connection
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import get_public_schema_name

from apps.guilds.admin import hevent
from apps.users.admin.inlines import ProfileInline, PrivateInline, CharInline
from apps.users.models import User
from helper.admin import PublicFullHide, DontLog


@admin.register(User, site=hevent)
class UserAdmin(DontLog, PublicFullHide, TenantAdminMixin, admin.ModelAdmin):
    list_display = ['__str__', 'date_created']
    search_fields = ['__str__']
    readonly_fields = ['date_created']
    list_select_related = ['profile']
    fieldsets = (
        ("Аккаунт", {
            'fields': (
                'username',
                'email',
                'is_global_admin',
                'date_created',
                'is_verified',
            )
        }),
    )
    inlines = [ProfileInline, PrivateInline, CharInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return connection.tenant.schema_name == get_public_schema_name()

