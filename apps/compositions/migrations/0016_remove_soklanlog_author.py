# Generated by Django 3.0.5 on 2020-05-12 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0015_auto_20200512_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soklanlog',
            name='author',
        ),
    ]
