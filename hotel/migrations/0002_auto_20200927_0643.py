# Generated by Django 3.1.1 on 2020-09-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=0),
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
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
