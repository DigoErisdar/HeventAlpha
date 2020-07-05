from datetime import date

from django.db import models
from image_cropping import ImageCropField, ImageRatioField

from helper.models import upload_image


class Profile(models.Model):
    user = models.OneToOneField('users.User', verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=25, blank=True, default="")
    date_birthday = models.DateField('День рождение', help_text='Год будет скрыт', blank=True, null=True)
    sex = models.CharField('Пол', max_length=6, choices=(('male', 'Мужской'), ('female', 'Женский')),
                           blank=True, null=True)

    def avatar_upload_image(self, filename):
        return upload_image(self, 'avatar', filename, self.user_id)

    avatar = ImageCropField("Аватар", blank=True, null=True, upload_to=avatar_upload_image)
    avatar_cropping = ImageRatioField('avatar', '124x124', verbose_name='Миниатюра')

    def wallpaper_upload_image(self, filename):
        return upload_image(self, 'wallpaper', filename, self.user_id)

    wallpaper = ImageCropField("Обложка", blank=True, null=True, upload_to=wallpaper_upload_image)
    wallpaper_cropping = ImageRatioField('wallpaper', '1920x624', verbose_name='Миниатюра')

    class Meta:
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"Профиль №{self.id}"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.date_birthday:
            self.date_birthday = date(2016, self.date_birthday.month, self.date_birthday.day)
        return super(Profile, self).save(force_insert, force_update, using, update_fields)
