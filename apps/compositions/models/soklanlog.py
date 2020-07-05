from django.db import models

from apps.compositions.choices import ACTION_CHOICES


class SoklanLog(models.Model):
    char = models.ForeignKey('chars.Char', verbose_name="Персонаж", on_delete=models.DO_NOTHING, editable=False)
    action = models.CharField("Событие", max_length=27, choices=ACTION_CHOICES, editable=False)
    date_created = models.DateTimeField('Дата', auto_now_add=True)
    comment = models.TextField('Комментарий', blank=True, default="")

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Действие соклана'
        verbose_name_plural = 'Действия соклан'

    def __str__(self):
        return f"{self.date_created}: {self.char.nickname} {self.get_action_display()}"
