# Generated by Django 3.1.1 on 2020-09-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20200927_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='arrival_time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]