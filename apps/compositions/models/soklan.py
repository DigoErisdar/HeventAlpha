from django.apps import apps
from django.db import models, connection
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.compositions.choices import ENTER, LEFT
from apps.compositions.managers.soklan import SoklanQuerySet


class Soklan(models.Model):
    char = models.OneToOneField('chars.Char', verbose_name='Персонаж', on_delete=models.DO_NOTHING)
    composition = models.ForeignKey('compositions.Composition', verbose_name="Состав", on_delete=models.CASCADE,
                                    related_name='soklans')
    rank = models.ForeignKey('compositions.rank', verbose_name="Звание", on_delete=models.CASCADE,
                             related_name='soklans')
    post = models.CharField('Должность', max_length=50, blank=True, default="")
    date_joined = models.DateTimeField("Дата приема в клан", auto_now_add=True, editable=False, db_index=True)
    permissions = models.ManyToManyField('auth.Permission', verbose_name="Права доступа", blank=True,
                                         related_name='soklans')
    is_admin = models.BooleanField('Администратор', help_text="Только администраторы имеют доступ в админ панель",
                                   default=False)

    objects = SoklanQuerySet.as_manager()

    class Meta:
        ordering = ['date_joined']
        verbose_name = 'Соклан'
        verbose_name_plural = 'Сокланы'

    def __str__(self):
        return self.char.nickname

    def delete(self, using=None, keep_parents=False, comment=""):
        SoklanLog = apps.get_model('compositions', 'SoklanLog')
        SoklanLog.objects.create(char_id=self.char_id, action=LEFT, comment=comment)
        return super(Soklan, self).delete(using, keep_parents)


@receiver(post_save, sender=Soklan)
def log_created_soklan(instance, created, **kwargs):
    if created:
        SoklanLog = apps.get_model('compositions', 'SoklanLog')
        SoklanLog.objects.create(char_id=instance.char_id, action=ENTER)


@receiver(post_save, sender=Soklan)
def set_char_tenant(instance, sender, created, update_fields, **kwargs):
    if created:
        instance.char.guild_id = connection.tenant.id
        instance.char.save(update_fields=['guild'])


@receiver(post_delete, sender=Soklan)
def del_char_tenant(instance, sender, **kwargs):
    if hasattr(instance.char, 'user') and instance.char.user is not None:
        instance.char.guild = None
        instance.char.save(update_fields=['guild'])
