# Generated by Django 3.0.8 on 2020-08-08 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]