from django.core.exceptions import ValidationError
from django.db import models
from django_tenants.utils import get_public_schema_name

from helper.models import get_slug


class Char(models.Model):
    user = models.ForeignKey("users.User", verbose_name="Владелец",
                             blank=True, null=True, on_delete=models.SET_NULL)
    guild = models.ForeignKey("guilds.Guild", verbose_name="Гильдия",
                              blank=True, null=True, on_delete=models.SET_NULL, editable=False)
    server = models.ForeignKey('pw.Server', on_delete=models.CASCADE, verbose_name="Сервер", default=1)
    nickname = models.CharField("Никнейм", help_text="Пожалуйста используйте копирабельные никнеймы", max_length=25)
    rase = models.ForeignKey("pw.Rase", verbose_name="Раса", on_delete=models.CASCADE)

    class Meta:
        ordering = ['nickname']
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
        unique_together = ['guild', 'nickname']

    def __str__(self):
        return self.nickname

    def full_clean(self, exclude=None, validate_unique=True):
        if self.guild is not None and self.guild.server != self.server:
            raise ValidationError({"server": "Гильдия и персонаж на разных серверах"})
        if self.guild is not None and self.guild.schema_name == get_public_schema_name():
            raise ValidationError({'server': "Это нельзя выбирать!"})

    @property
    def slug(self):
        return get_slug(self.nickname)