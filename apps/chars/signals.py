from django.db.models.signals import post_init, post_save, pre_delete
from django.dispatch import receiver
from django_tenants.utils import get_public_schema_name, schema_context

from apps.chars.models import Char, InviteChar
from apps.compositions.models import Soklan, SoklanLog
from apps.constrforms.models import Claim
from apps.guilds.models import Guild


@receiver(post_init, sender=Char)
def pre_instance_char(sender, instance, **kwargs):
    instance.original_guild = instance.guild_id
    instance.original_user = instance.user_id


@receiver(post_save, sender=Char)
def change_user_guild(sender, instance, update_fields, created, **kwargs):
    if hasattr(instance, 'user') and instance.user is not None \
            and instance.user_id != instance.original_user:
        if hasattr(instance, 'invite'):
            instance.invite.generate_token()


@receiver(pre_delete, sender=Char)
def cascade_delete(sender, instance, *args, **kwargs):
    guilds = Guild.objects.exclude(schema_name=get_public_schema_name()).all()
    for guild in guilds:
        with schema_context(guild.schema_name):
            Soklan.objects.filter(char_id=instance.pk).delete()
            InviteChar.objects.filter(char_id=instance.pk).delete()
            Claim.objects.filter(char_id=instance.pk).delete()
            SoklanLog.objects.filter(char_id=instance.pk).delete()
