# Generated by Django 3.0.3 on 2020-06-27 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200526_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='gender',
            new_name='sex',
        ),
    ]