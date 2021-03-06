# Generated by Django 3.1.1 on 2020-10-22 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField(null=True)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('specials', models.TextField(max_length=256, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('twin', 'Twin Room'), ('dbl', 'Double Room'), ('fam', 'Family Room'), ('dsui', 'Deluxe Suite'), ('apt', 'Apartment'), ('dapt', 'Deluxe Apartment')], max_length=25)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('children_capacity', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.unit'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
