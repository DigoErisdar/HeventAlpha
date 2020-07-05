from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.guilds.models import Domain


@receiver(post_save, sender=Domain)
def create_rank(sender, instance, created, **kwargs):
    if created:
        instance.tenant.create_rank()