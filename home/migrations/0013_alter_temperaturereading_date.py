# Generated by Django 3.2.5 on 2021-07-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210716_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturereading',
            name='date',
            field=models.DateTimeField(blank=True, default='2021-07-16T18:56:19'),
        ),
    ]
