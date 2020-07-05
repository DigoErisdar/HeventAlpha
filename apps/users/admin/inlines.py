from django.contrib import admin
from image_cropping import ImageCroppingMixin

from apps.chars.models import Char
from apps.users.choices import FIELD_CHOICES
from apps.users.models import Private, Profile


class CharInline(admin.TabularInline):
    model = Char
    max_num = 5
    min_num = 0
    extra = 1
    can_delete = False
    verbose_name = "Персонаж"
    autocomplete_fields = ['rase', 'guild', 'server']
    fields = ['nickname', 'rase', 'server']


class ProfileInline(ImageCroppingMixin, admin.StackedInline):
    model = Profile
    max_num = 1
    min_num = 1
    extra = 1
    can_delete = False
    verbose_name = "Профиль"


class PrivateInline(admin.TabularInline):
    model = Private
    can_delete = False
    max_num = len(FIELD_CHOICES)
    min_num = len(FIELD_CHOICES)
    radio_fields = {"value": admin.HORIZONTAL}
    verbose_name = "Приватность"
    readonly_fields = ['field']
    fields = ['field', 'value']