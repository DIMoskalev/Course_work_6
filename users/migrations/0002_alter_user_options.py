# Generated by Django 4.2.2 on 2024-08-05 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email', 'first_name', 'last_name'), 'permissions': [('view_users', 'Can view all users'), ('block_users', 'Can block all users')], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
