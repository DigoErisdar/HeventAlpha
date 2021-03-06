# Generated by Django 3.0.5 on 2020-05-17 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constrforms', '0012_auto_20200517_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicefield',
            name='widget',
            field=models.CharField(choices=[('Одиночный выбор', (('field', 'Поле'), ('radio', 'Радиокнопки'))), ('Множественный выбор', (('multifield', 'Поле'), ('checkbox', 'Чекбоксы')))], default='field', max_length=25, verbose_name='Вид'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='form',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='constrforms.CustomForm', verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='request',
            name='text',
            field=models.TextField(blank=True, default='', editable=False, verbose_name='Текст'),
        ),
    ]
