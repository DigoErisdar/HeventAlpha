# Generated by Django 3.0.5 on 2020-05-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constrforms', '0009_auto_20200517_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicesforfield',
            name='type',
        ),
        migrations.RemoveField(
            model_name='imagefield',
            name='type',
        ),
        migrations.RemoveField(
            model_name='integerfield',
            name='type',
        ),
        migrations.RemoveField(
            model_name='textfield',
            name='type',
        ),
        migrations.AddField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('text', 'Текст'), ('int', 'Целочисленный'), ('choice', 'Выбор'), ('img', 'Изображение')], default='text', editable=False, max_length=15, verbose_name='Тип'),
        ),
    ]
