# Generated by Django 3.0.8 on 2020-08-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
