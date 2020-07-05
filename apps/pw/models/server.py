from django.db import models

from helper.models import get_slug


class Server(models.Model):
    title = models.CharField('Название', max_length=25, unique=True)
    sort = models.PositiveSmallIntegerField("", default=0)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Сервер'
        verbose_name_plural = 'Сервера'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return get_slug(self.title)