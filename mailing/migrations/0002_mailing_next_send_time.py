# Generated by Django 4.2.2 on 2024-08-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_send_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время следующей отправки'),
        ),
    ]
