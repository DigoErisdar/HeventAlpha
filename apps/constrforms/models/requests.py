from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from django.urls import reverse

from apps.constrforms.managers import RequestQuerySet


class Claim(models.Model):
    form = models.ForeignKey('constrforms.CustomForm', verbose_name="Форма", on_delete=models.CASCADE,
                             related_name='requests')
    char = models.ForeignKey('chars.Char', verbose_name="Персонаж", on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    text = models.TextField(verbose_name="Текст", default="", blank=True, editable=False)
    status = models.ForeignKey('constrforms.RequestStatus', verbose_name="Статус",
                               blank=True, null=True, on_delete=models.SET_NULL)
    is_close = models.BooleanField('Закрыта', default=False)

    objects = RequestQuerySet.as_manager()

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"{self.form} от {self.char.nickname} {self.char.rase.title}"

    def get_absolute_url(self):
        return reverse("requests:request", kwargs={'slug': self.form.slug, 'pk': self.pk})

    def get_card(self):
        return get_template("constrforms/includes/card-requests.html").render({'request': self})


@receiver(post_save, sender=Claim)
def change_status(instance, sender, created, **kwargs):
    if created:
        instance.status = instance.form.default_status
        instance.save(update_fields=['status'])
    else:
        instance.original_status = instance.status

