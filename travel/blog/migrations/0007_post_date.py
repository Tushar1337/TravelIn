# Generated by Django 3.0.8 on 2020-08-20 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
