# Generated by Django 3.2.5 on 2021-07-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_humidityreading_temperaturereading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidityreading',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='temperaturereading',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
