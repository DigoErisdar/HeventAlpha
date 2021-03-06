# Generated by Django 3.0.5 on 2020-05-11 14:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0013_auto_20200511_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='close_loot',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), default=list, size=7, verbose_name='Лут закрыт в'),
        ),
        migrations.AddField(
            model_name='composition',
            name='user_attempts',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Заявок на итемки у пользователя'),
        ),
    ]
