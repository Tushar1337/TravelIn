# Generated by Django 3.0.8 on 2020-08-10 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200810_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.DayItenary'),
        ),
    ]
