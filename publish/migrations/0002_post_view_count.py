# Generated by Django 4.2.7 on 2023-11-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='View Count'),
        ),
    ]
