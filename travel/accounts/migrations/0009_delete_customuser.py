# Generated by Django 3.0.8 on 2020-08-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
