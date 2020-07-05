from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

from helper.models import get_slug


class Composition(models.Model):
    title = models.CharField("Название", max_length=25, unique=True)
    sort = models.PositiveSmallIntegerField("", default=0)
    close_loot = ArrayField(
        models.CharField(max_length=1),
        verbose_name="Лут закрыт в",
        default=list, size=7
    )
    user_attempts = models.PositiveSmallIntegerField('Заявок на итемки у пользователя', default=0, blank=True)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return get_slug(self.title)

    def has_loot_open(self):
        weekday = datetime.now().date().isoweekday()
        return str(weekday) not in self.close_loot
