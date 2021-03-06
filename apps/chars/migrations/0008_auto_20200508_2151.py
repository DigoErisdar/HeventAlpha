# Generated by Django 3.0.5 on 2020-05-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0001_initial'),
        ('chars', '0007_auto_20200508_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='char',
            name='guild',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='guilds.Guild', verbose_name='Гильдия'),
        ),
        migrations.CreateModel(
            name='InviteChar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True, verbose_name='Токен')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('char', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chars.Char', verbose_name='Персонаж')),
            ],
            options={
                'verbose_name': 'Реферальный аккаунт',
                'verbose_name_plural': 'Реферальные аккаунты',
                'ordering': ['-date_created'],
            },
        ),
    ]
