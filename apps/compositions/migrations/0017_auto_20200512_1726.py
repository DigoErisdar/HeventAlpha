# Generated by Django 3.0.5 on 2020-05-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('compositions', '0016_remove_soklanlog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='ranks', to='auth.Permission', verbose_name='Права доступа'),
        ),
        migrations.AlterField(
            model_name='soklan',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='soklans', to='auth.Permission', verbose_name='Права доступа'),
        ),
    ]
