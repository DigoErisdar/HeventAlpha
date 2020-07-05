# Generated by Django 3.0.5 on 2020-05-05 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0001_initial'),
        ('chars', '0002_auto_20200504_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='char',
            name='guild',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guilds.Guild', verbose_name='Гильдия'),
        ),
    ]