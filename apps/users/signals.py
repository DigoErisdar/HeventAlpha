from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.choices import FIELD_CHOICES
from apps.users.models import User
from apps.users.models.private import Private
from apps.users.models.profile import Profile


@receiver(post_save, sender=User)
def create_user(sender, instance, created, update_fields, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        privates = [Private(user=instance, field=private[0]) for private in FIELD_CHOICES]
        Private.objects.bulk_create(privates, ignore_conflicts=True)