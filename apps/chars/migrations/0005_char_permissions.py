# Generated by Django 3.0.5 on 2020-05-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('chars', '0004_auto_20200506_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='char',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='Права'),
        ),
    ]