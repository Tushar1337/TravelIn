# Generated by Django 3.0.8 on 2020-08-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_packages_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.DayItenary'),
        ),
    ]
