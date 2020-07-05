from django.apps import apps
from django.db import models

from apps.compositions.choices import LEFT


class SoklanQuerySet(models.QuerySet):

    def delete(self, comment=""):
        SoklanLog = apps.get_model('compositions', 'SoklanLog')
        logs = [SoklanLog(char_id=soklan.char_id, action=LEFT, comment=comment) for soklan in self.iterator()]
        SoklanLog.objects.bulk_create(logs, ignore_conflicts=True)
        return super(SoklanQuerySet, self).delete()