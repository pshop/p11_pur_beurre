# Generated by Django 2.1.2 on 2018-12-18 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181218_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetlink',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 14, 46, 32, 273549)),
        ),
        migrations.AlterField(
            model_name='resetlink',
            name='link_id',
            field=models.CharField(max_length=150),
        ),
    ]
