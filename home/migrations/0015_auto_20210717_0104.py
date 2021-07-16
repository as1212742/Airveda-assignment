# Generated by Django 3.2.5 on 2021-07-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_temperaturereading_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidityreading',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='temperaturereading',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]