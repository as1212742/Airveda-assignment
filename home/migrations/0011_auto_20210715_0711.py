# Generated by Django 3.2.5 on 2021-07-15 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210715_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidityreading',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 15, 7, 11, 47, 701760)),
        ),
        migrations.AlterField(
            model_name='temperaturereading',
            name='date',
            field=models.DateTimeField(blank=True, default='2021-07-15T07:11:47'),
        ),
    ]
