from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.constrforms.choices import TYPE_FIELD, WIDGET_FIELD


class Field(models.Model):
    label = models.CharField('Название', max_length=35)
    help_text = models.CharField('Подсказка', max_length=75, blank=True, default="")
    required = models.BooleanField('Обязательное поле', default=False)
    type = models.CharField('Тип', default='text', choices=TYPE_FIELD, editable=False, max_length=15)

    class Meta:
        ordering = ['label']
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'

    def __str__(self):
        return self.label


class TextField(Field):
    is_multiline = models.BooleanField('Многострочное поле', default=False)

    class Meta:
        ordering = ['label']
        verbose_name = 'Текстовое поле'
        verbose_name_plural = 'Текстовые поля'


class IntegerField(Field):
    min = models.IntegerField('Минимальное значение')
    max = models.IntegerField('Максимальное значение')

    class Meta:
        ordering = ['label']
        verbose_name = 'Числовое поле'
        verbose_name_plural = 'Числовые поля'

    def __str__(self):
        return f"{self.label} {self.min} - {self.max}"


class ChoicesForField(models.Model):
    title = models.CharField('Название', max_length=55, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.title


class ChoiceField(Field):
    choices = models.ManyToManyField('constrforms.ChoicesForField', verbose_name="Варианты выбора")
    widget = models.CharField('Вид', max_length=25, choices=WIDGET_FIELD)

    class Meta:
        ordering = ['label']
        verbose_name = 'Поле выбора'
        verbose_name_plural = 'Поля выбора'

    def __str__(self):
        return self.label


class ImageField(Field):
    pass

    class Meta:
        ordering = ['label']
        verbose_name = 'Поле изображения'
        verbose_name_plural = 'Поля изображений'

    def __str__(self):
        return self.label


@receiver(post_save, sender=IntegerField)
@receiver(post_save, sender=ChoiceField)
@receiver(post_save, sender=ImageField)
def set_type_field(instance, sender, created, **kwargs):
    if created:
        types = {
            'IntegerField': 'int',
            'ChoiceField': 'choice',
            'ImageField': 'img',
        }
        type_field = types.get(sender.__name__, 'text')
        instance.type = type_field
        instance.save(update_fields=['type'])
