# Generated by Django 3.2.5 on 2021-07-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_temperaturereading_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturereading',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
