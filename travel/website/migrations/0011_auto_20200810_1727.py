# Generated by Django 3.0.8 on 2020-08-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_dayitenary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayitenary',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
