# Generated by Django 3.0.5 on 2020-05-06 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0004_auto_20200506_1149'),
        ('compositions', '0005_auto_20200505_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soklan',
            name='char',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='chars.Char', verbose_name='Персонаж'),
        ),
    ]
