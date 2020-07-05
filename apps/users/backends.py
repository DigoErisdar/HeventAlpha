from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import Permission
from django.db import connection
from django.db.models import Exists, Q, OuterRef
from django_tenants.utils import get_public_schema_name

from apps.compositions.models import Soklan

UserModel = get_user_model()


class UserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return None
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            user = UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user

    def _get_user_permissions(self, user_obj):
        if connection.tenant.schema_name != get_public_schema_name():
            return Permission.objects.filter(soklans__char__user=user_obj).distinct().all()
        else:
            return Permission.objects.all()

    def _get_group_permissions(self, user_obj):
        if connection.tenant.schema_name != get_public_schema_name():
            return Permission.objects.filter(ranks__soklans__char__user=user_obj).all()
        else:
            return Permission.objects.all()

    def _get_permissions(self, user_obj, obj, from_name):
        """
        Return the permissions of `user_obj` from `from_name`. `from_name` can
        be either "group" or "user" to return permissions from
        `_get_group_permissions` or `_get_user_permissions` respectively.
        """
        if user_obj.is_anonymous or obj is not None:
            return set()

        perm_cache_name = '_%s_perm_cache' % from_name
        if not hasattr(user_obj, perm_cache_name):
            # TODO: delete blocked permissions for global admin
            if user_obj.is_global_admin and False:
                perms = Permission.objects.all()
            else:
                perms = getattr(self, '_get_%s_permissions' % from_name)(user_obj)
            perms = perms.values_list('content_type__app_label', 'codename').order_by()
            setattr(user_obj, perm_cache_name, {"%s.%s" % (ct, name) for ct, name in perms})
        return getattr(user_obj, perm_cache_name)

    def get_user_permissions(self, user_obj, obj=None):
        """
        Return a set of permission strings the user `user_obj` has from their
        `user_permissions`.
        """
        return self._get_permissions(user_obj, obj, 'user')

    def get_group_permissions(self, user_obj, obj=None):
        """
        Return a set of permission strings the user `user_obj` has from the
        groups they belong.
        """
        return self._get_permissions(user_obj, obj, 'group')

    def get_all_permissions(self, user_obj, obj=None):
        if connection.tenant.schema_name != get_public_schema_name():
            if not (user_obj.is_authenticated and Soklan.objects.filter(char__user=user_obj).exists()):
                return set()
        if not hasattr(user_obj, '_perm_cache'):
            user_obj._perm_cache = super().get_all_permissions(user_obj)
        return user_obj._perm_cache

    def has_perm(self, user_obj, perm, obj=None):
        return super().has_perm(user_obj, perm, obj=obj)

    def has_module_perms(self, user_obj, app_label):
        """
        Return True if user_obj has any permissions in the given app_label.
        """
        return any(
            perm[:perm.index('.')] == app_label
            for perm in self.get_all_permissions(user_obj)
        )

    def with_perm(self, perm, is_active=True, include_superusers=True, obj=None):
        """
        Return users that have permission "perm". By default, filter out
        inactive users and include superusers.
        """
        if isinstance(perm, str):
            try:
                app_label, codename = perm.split('.')
            except ValueError:
                raise ValueError(
                    'Permission name should be in the form '
                    'app_label.permission_codename.'
                )
        elif not isinstance(perm, Permission):
            raise TypeError(
                'The `perm` argument must be a string or a permission instance.'
            )

        UserModel = get_user_model()
        if obj is not None:
            return UserModel._default_manager.none()
        permission_q = Q(group__user=OuterRef('pk')) | Q(user=OuterRef('pk'))
        if isinstance(perm, Permission):
            permission_q &= Q(pk=perm.pk)
        else:
            permission_q &= Q(codename=codename, content_type__app_label=app_label)

        user_q = Exists(Permission.objects.filter(permission_q))
        if include_superusers:
            user_q |= Q(is_global_admin=True)

        return UserModel._default_manager.filter(user_q)