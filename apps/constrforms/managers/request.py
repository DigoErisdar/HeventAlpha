from django.apps import apps
from django.db import models, connection
from django_tenants.utils import get_public_schema_name, schema_context

from apps.compositions.choices import CONFIRM, WAIT, SOLIDER, ENTER
from apps.compositions.models import Soklan


class RequestQuerySet(models.QuerySet):

    def accept(self, composition):
        # init
        Request = apps.get_model("compositions", "Request")
        Guild = apps.get_model('guilds', 'Guild')
        Rank = apps.get_model('compositions', 'Rank')
        SoklanLog = apps.get_model('compositions', 'SoklanLog')
        Char = apps.get_model('chars', 'Char')
        rank = Rank.objects.get(title=SOLIDER).id
        # confirm chars
        chars = list(self.values_list('char_id', flat=True))
        soklans = [Soklan(char_id=char, composition_id=int(composition), rank_id=rank) for char in chars]
        soklans = Soklan.objects.bulk_create(soklans, ignore_conflicts=True)
        logs = [SoklanLog(char_id=soklan.char_id, action=ENTER) for soklan in soklans]
        SoklanLog.objects.bulk_create(logs, ignore_conflicts=True)
        self.update(status=CONFIRM)
        Char.objects.filter(id__in=chars).update(guild_id=connection.tenant.id)
        # clear old request other guild
        guilds = Guild.objects.exclude(
            schema_name__in=[get_public_schema_name(), connection.tenant.schema_name])
        for guild in guilds.iterator():
            with schema_context(guild.schema_name):
                Request.objects.filter(char_id__in=chars, status=WAIT).delete()
        return self
