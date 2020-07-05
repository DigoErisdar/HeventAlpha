from django.db import models

from apps.compositions.choices import RANK_CHOICES


class Rank(models.Model):
    title = models.CharField("Название", max_length=25, unique=True, choices=RANK_CHOICES)
    permissions = models.ManyToManyField('auth.Permission', verbose_name="Права доступа", blank=True,
                                         related_name='ranks')
    sort = models.PositiveSmallIntegerField('', default=0)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'

    def __str__(self):
        return self.get_title_display()

    @property
    def slug(self):
        return self.title
