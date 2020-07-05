# Generated by Django 3.0.5 on 2020-05-19 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constrforms', '0016_auto_20200518_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestpage',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='request',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='constrforms.CustomForm', verbose_name='Форма'),
        ),
    ]