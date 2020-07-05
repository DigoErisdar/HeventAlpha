from django.db import models


class FeedBack(models.Model):
    message = models.TextField('Сообщение')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.message
