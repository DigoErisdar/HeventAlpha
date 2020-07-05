from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django_tenants.utils import get_public_schema_name

from apps.compositions.models import Soklan
from apps.users.choices import SOKLAN, FIELDS, ALL


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_global_admin', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_global_admin', False)
        return self._create_user(username, email, password, **extra_fields)

    def get_private_fields(self, users, request) -> dict:
        """Возвращает список доступных полей для списка пользователей"""
        # Инициализация
        visitor = request.user
        Private = apps.get_model('users', 'Private')

        fields = {}
        for field in FIELDS.keys():
            fields[field] = {visitor.id}

        # Добавление полей доступных всем
        for private in Private.objects.filter(user__in=users, value=ALL):
            fields[private.field].add(private.user_id)

        # Добавление полей доступных для админов
        if visitor.is_authenticated and visitor.is_global_admin or (
            request.tenant.schema_name != get_public_schema_name()
            and Soklan.objects.filter(char__user_id=visitor.id, is_admin=True).exists()
        ):
            ids = users.values_list('id', flat=True)
            for field in fields.values():
                field |= set(ids)

        # Добавление полей доступных для соклан
        if request.tenant.schema_name != get_public_schema_name() and Soklan.objects.filter(char__user=visitor).exists():
            soklans = Private.objects.filter(user__in=users, value=SOKLAN, user__char__soklan__isnull=False)
            for private in soklans.iterator():
                fields[private.field].add(private.user_id)

        return fields
