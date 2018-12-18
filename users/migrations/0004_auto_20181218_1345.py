# Generated by Django 2.1.2 on 2018-12-18 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_resetlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetlink',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 14, 45, 51, 456912)),
        ),
        migrations.AlterField(
            model_name='resetlink',
            name='link_id',
            field=models.CharField(max_length=33),
        ),
    ]
