from django.contrib import admin
from image_cropping import ImageCroppingMixin

from apps.guilds.models import Profile


class ProfileInline(ImageCroppingMixin, admin.StackedInline):
    model = Profile
    extra = 1
    max_num = extra
    min_num = extra
    verbose_name = 'Профиль'
    can_delete = False
