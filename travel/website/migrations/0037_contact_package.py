# Generated by Django 3.0.8 on 2020-08-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_auto_20200811_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='package',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
