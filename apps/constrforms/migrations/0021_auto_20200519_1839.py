# Generated by Django 3.0.5 on 2020-05-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constrforms', '0020_auto_20200519_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requeststatus',
            name='action',
        ),
        migrations.AddField(
            model_name='requeststatus',
            name='action_char',
            field=models.CharField(blank=True, choices=[('invite', 'Принять в клан')], max_length=25, null=True, verbose_name='Действие для персонажа'),
        ),
        migrations.AddField(
            model_name='requeststatus',
            name='action_request',
            field=models.CharField(blank=True, choices=[('open', 'Открыть'), ('close', 'Закрыть')], max_length=25, null=True, verbose_name='Действие для заявки'),
        ),
    ]
