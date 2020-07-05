# Generated by Django 3.0.5 on 2020-05-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constrforms', '0003_auto_20200511_1900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ['label'], 'verbose_name': 'Поле', 'verbose_name_plural': 'Поля'},
        ),
        migrations.AlterModelOptions(
            name='integerfield',
            options={'ordering': ['label'], 'verbose_name': 'Числовое поле', 'verbose_name_plural': 'Числовые поля'},
        ),
        migrations.AlterModelOptions(
            name='requestformmodel',
            options={'ordering': ['sort'], 'verbose_name': 'Поле формы заявки', 'verbose_name_plural': 'Поля формы заявки'},
        ),
        migrations.AlterModelOptions(
            name='textfield',
            options={'ordering': ['label'], 'verbose_name': 'Текстовое поле', 'verbose_name_plural': 'Текстовые поля'},
        ),
        migrations.AddField(
            model_name='requestformmodel',
            name='sort',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=''),
        ),
    ]