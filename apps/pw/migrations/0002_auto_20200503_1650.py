# Generated by Django 3.0.5 on 2020-05-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pw', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rase',
            options={'ordering': ['sort'], 'verbose_name': 'Раса', 'verbose_name_plural': 'Расы'},
        ),
    ]
