# Generated by Django 3.0.5 on 2020-05-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0012_auto_20200512_1438'),
        ('constrforms', '0024_requeststatus_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Claim',
        ),
        migrations.AlterField(
            model_name='requeststatus',
            name='color',
            field=models.CharField(blank=True, choices=[('primary', 'Синий'), ('secondary', 'Серый'), ('success', 'Зеленый'), ('danger', 'Красный'), ('warning', 'Желтый'), ('light', 'Белый'), ('dark', 'Черный')], default='', max_length=25, verbose_name='Цвет'),
        ),
    ]
