from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import _user_get_permissions, _user_has_perm, _user_has_module_perms
from django.db import models
from django.urls import reverse
from django_tenants.utils import get_public_schema_name

from apps.compositions.models import Soklan
from apps.users.choices import ALL, ADMIN, SOKLAN
from apps.users.managers import UserManager
from helper.models import get_slug


class User(AbstractBaseUser):
    username = models.CharField("Логин", max_length=27, unique=True, db_index=True)
    email = models.EmailField('Электронная почта', unique=True, help_text="Необходима для восстановления пароля")
    is_global_admin = models.BooleanField("Глобальный администратор", default=False)
    is_verified = models.BooleanField("Подтвержден", default=False)
    date_created = models.DateTimeField("Дата регистрации", auto_now_add=True, db_index=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def slug(self):
        return get_slug(self.__str__())

    def get_nickname(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"slug": self.slug, "pk": self.pk})

    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'user')

    def get_group_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'group')

    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')

    def has_perm(self, perm, obj=None):
        if self.is_global_admin:
            return True
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        if self.is_global_admin:
            return True

        return _user_has_module_perms(self, app_label)

    def is_user_admin(self, request):
        return self.is_global_admin or (
                request.tenant.schema_name != get_public_schema_name()
                and Soklan.objects.filter(char__user_id=self.id, is_admin=True).exists()
        )
