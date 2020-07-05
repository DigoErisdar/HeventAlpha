from django.db import models

from apps.users.choices import FIELD_CHOICES, VALUE_CHOICES, ALL


class Private(models.Model):
    user = models.ForeignKey('users.User', verbose_name="Пользователь", on_delete=models.CASCADE,
                             related_name='privates')
    field = models.CharField('Поле', max_length=25, choices=FIELD_CHOICES)
    value = models.CharField('Значение', max_length=25, choices=VALUE_CHOICES, default=ALL)

    class Meta:
        ordering = ['user', 'field']
        verbose_name = 'Поле приватности'
        verbose_name_plural = 'Поля приватности'
        unique_together = ['user', 'field']

    def __str__(self):
        return f"{self.user.__str__()}:{self.get_field_display()} видно {self.get_value_display()}"
