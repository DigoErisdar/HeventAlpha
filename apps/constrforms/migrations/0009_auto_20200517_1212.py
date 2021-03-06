# Generated by Django 3.0.5 on 2020-05-17 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constrforms', '0008_auto_20200517_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicesforfield',
            name='type',
            field=models.CharField(choices=[('text', 'Текст'), ('int', 'Целочисленный'), ('choice', 'Выбор'), ('img', 'Изображение')], default='choice', editable=False, max_length=15, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='imagefield',
            name='type',
            field=models.CharField(choices=[('text', 'Текст'), ('int', 'Целочисленный'), ('choice', 'Выбор'), ('img', 'Изображение')], default='img', editable=False, max_length=15, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='integerfield',
            name='type',
            field=models.CharField(choices=[('text', 'Текст'), ('int', 'Целочисленный'), ('choice', 'Выбор'), ('img', 'Изображение')], default='int', editable=False, max_length=15, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='textfield',
            name='type',
            field=models.CharField(choices=[('text', 'Текст'), ('int', 'Целочисленный'), ('choice', 'Выбор'), ('img', 'Изображение')], default='text', editable=False, max_length=15, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='constrforms.CustomForm', verbose_name='Форма'),
        ),
    ]
