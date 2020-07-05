from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from apps.chars.models import Char
from helper.models import get_unique_token

class InviteChar(models.Model):
    char = models.OneToOneField(Char, on_delete=models.DO_NOTHING, verbose_name="Персонаж", related_name='invite')
    slug = models.SlugField("Токен", max_length=250, editable=False, unique=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    creator = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, verbose_name="Создатель", editable=False)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Реферальный аккаунт'
        verbose_name_plural = 'Реферальные аккаунты'

    def __str__(self):
        return self.char.__str__()

    def get_absolute_url(self):
        return reverse('users:invite', kwargs={'slug': self.slug})

    def generate_token(self):
        self.slug = get_unique_token(obj=self, field='slug')
        self.save(update_fields=['slug'])

    def full_clean(self, exclude=None, validate_unique=True):
        if not self.char:
            raise ValidationError("Необходимо заполнить персонажа")
        if not self.slug:
            self.slug = get_unique_token(obj=self, field='slug')
