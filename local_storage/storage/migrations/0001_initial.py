# Generated by Django 3.1.6 on 2021-02-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='Сайт:')),
                ('login', models.CharField(max_length=255, verbose_name='Логин')),
                ('passwd', models.CharField(max_length=255, verbose_name='Пароль')),
                ('two_auth', models.BooleanField(default=False, verbose_name='Двухфакторная аутентификация')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
    ]
