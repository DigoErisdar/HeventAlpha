from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from helper.models import get_slug


class CustomForm(models.Model):
    title = models.CharField('Название', max_length=25, unique=True)
    default_status = models.OneToOneField('constrforms.RequestStatus', on_delete=models.SET_NULL, blank=True, null=True,
                                          verbose_name="Статус по умолчанию")

    class Meta:
        ordering = ['title']
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return get_slug(self.title)

    def get_absolute_url(self):
        return reverse("requests:form", kwargs={'slug': self.slug, 'pk': self.pk})

    def clean(self):
        if self.default_status is not None and self.default_status.form_id != self.id:
            raise ValidationError({'default_status': "Выбранный статус не принадлежит форме"})


class FormField(models.Model):
    form = models.ForeignKey('constrforms.CustomForm', verbose_name='Форма', on_delete=models.CASCADE,
                             related_name='fields')
    field = models.ForeignKey('constrforms.Field', verbose_name="Поле", on_delete=models.CASCADE)
    sort = models.PositiveSmallIntegerField('', default=0)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Поле формы'
        verbose_name_plural = 'Поля формы'
        unique_together = ['form', 'field']

    def __str__(self):
        return self.field.label
