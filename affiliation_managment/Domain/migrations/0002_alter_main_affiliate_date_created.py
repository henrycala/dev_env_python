# Generated by Django 3.2.4 on 2021-06-14 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Domain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_affiliate',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
