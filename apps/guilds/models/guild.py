from django.db import models
from django_tenants.models import TenantMixin
from django_tenants.utils import tenant_context

from apps.compositions.choices import RANK_CHOICES
from apps.compositions.models import Rank
from helper.models import get_slug
from system import settings


class Guild(TenantMixin):
    server = models.ForeignKey("pw.Server", on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name="Сервер")
    name = models.CharField(max_length=100, verbose_name="Название")
    created_on = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    auto_drop_schema = True

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Гильдия'
        verbose_name_plural = 'Гильдии'
        unique_together = ['server', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        domain = f"{self.schema_name}.{settings.DOMAIN}"
        port = ":8000" if settings.DOMAIN == 'localhost' else ""
        protocol = "http" if settings.DOMAIN == 'localhost' else "https:"
        return f"{protocol}://{domain}{port}"

    @property
    def slug(self):
        return get_slug(self.name)

    def create_rank(self):
        ranks = [Rank(title=rank[0]) for rank in RANK_CHOICES]
        with tenant_context(self):
            Rank.objects.bulk_create(ranks, ignore_conflicts=True)

