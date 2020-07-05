from django.db import models
from django.urls import reverse

from helper.models import get_slug


class RequestPage(models.Model):
    title = models.CharField("Название страницы", unique=True, max_length=75)
    form = models.OneToOneField('constrforms.CustomForm', verbose_name="Форма", on_delete=models.CASCADE)
    description = models.TextField('Описание', blank=True, default="")

    class Meta:
        ordering = ['title']
        verbose_name = 'Страница с заявкой'
        verbose_name_plural = 'Страницы с заявками'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return get_slug(self.title)

    def get_absolute_url(self):
        return f"/{self.slug}.{self.pk}/"



