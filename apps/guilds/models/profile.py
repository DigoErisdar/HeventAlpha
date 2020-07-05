from django.db import models
from image_cropping import ImageRatioField

from helper.models import upload_image


class Profile(models.Model):
    guild = models.OneToOneField('guilds.Guild', verbose_name="Гильдия", on_delete=models.CASCADE)

    def favicon_logo_upload(self, filename):
        return upload_image(self, 'favicon', filename, self.guild_id)

    favicon = models.ImageField('favicon', upload_to=favicon_logo_upload, blank=True, null=True)

    def tenant_logo_upload(self, filename):
        return upload_image(self, 'logo', filename, self.guild_id)

    logo = models.ImageField(blank=True, upload_to=tenant_logo_upload, verbose_name="Логотип", null=True)
    cropping = ImageRatioField('logo', '120x120', verbose_name="Миниатюра")

    def wall_logo_upload(self, filename):
        return upload_image(self, 'wall', filename, self.guild_id)

    wall = models.ImageField(blank=True, upload_to=wall_logo_upload, verbose_name="Обложка", null=True)
    wall_cropping = ImageRatioField('wall', '1368x472', verbose_name="Миниатюра")

    description = models.TextField('Описание', blank=True, default="")

    class Meta:
        ordering = ['guild']
        verbose_name = 'Профиль гильдии'
        verbose_name_plural = 'Профили гильдий'

    def __str__(self):
        return self.guild.name

    def get_favicon(self):
        if self.favicon:
            return self.favicon.url
        else:
            return '/static/img/base/favicon.png'
