# Generated by Django 3.0.8 on 2020-08-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_destination_desc1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='offer',
        ),
        migrations.AddField(
            model_name='packages',
            name='highlight',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='highlight1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='highlight2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='highlight3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
