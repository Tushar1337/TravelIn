# Generated by Django 3.0.8 on 2020-08-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]