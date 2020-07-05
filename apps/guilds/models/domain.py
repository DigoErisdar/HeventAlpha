from django_tenants.models import DomainMixin


class Domain(DomainMixin):
    class Meta:
        verbose_name = 'Домен'
        verbose_name_plural = 'Домены'

    def __str__(self):
        return self.domain
