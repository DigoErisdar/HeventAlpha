from django.apps import AppConfig


class CharsConfig(AppConfig):
    name = 'apps.chars'
    verbose_name = 'Персонажи'

    def ready(self):
        from . import signals
