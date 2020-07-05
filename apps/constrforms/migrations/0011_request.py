# Generated by Django 3.0.5 on 2020-05-17 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chars', '0012_auto_20200512_1438'),
        ('constrforms', '0010_auto_20200517_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(blank=True, default='', verbose_name='Текст')),
                ('status', models.CharField(choices=[('wait', 'Ожидание'), ('confirm', 'Принят'), ('cancel', 'Отклонено')], default='wait', editable=False, max_length=27, verbose_name='Статус')),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chars.Char', verbose_name='Персонаж')),
            ],
            options={
                'verbose_name': 'Заявка в клан',
                'verbose_name_plural': 'Заявки в клан',
                'ordering': ['-date_created'],
            },
        ),
    ]
