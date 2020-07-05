from django.db import models
from django.utils.html import format_html

from apps.constrforms.choices import REQUEST_ACTION, CHAR_ACTION
from helper.choices import COLOR_CHOICES


class RequestStatus(models.Model):
    title = models.CharField('Название', max_length=25)
    form = models.ForeignKey('constrforms.CustomForm', on_delete=models.CASCADE, verbose_name="Форма",
                             related_name='statuses')
    color = models.CharField('Цвет', max_length=25, blank=True, default="", choices=COLOR_CHOICES)
    action_request = models.CharField('Действие для заявки', max_length=25, choices=REQUEST_ACTION,
                                      blank=True, null=True)
    action_char = models.CharField('Действие для персонажа', max_length=25, choices=CHAR_ACTION,
                                   blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        unique_together = ['form', 'title']

    def __str__(self):
        return self.title

    def get_color(self):
        cls = ['badge']
        if self.color:
            cls.append('badge-' + self.color)
        return format_html(f'<span class="{" ".join(cls)}">{self.title}</span>')
