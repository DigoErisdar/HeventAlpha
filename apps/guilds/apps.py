from django.apps import AppConfig


class GuildsConfig(AppConfig):
    name = 'apps.guilds'
    verbose_name = 'Гильдия'
    verbose_name_plural = 'Гильдии'

    def ready(self):
        from . import signals
