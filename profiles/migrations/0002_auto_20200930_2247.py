# Generated by Django 3.1.1 on 2020-09-30 22:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_booking_user_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LocalUser',
            new_name='CreateProfile',
        ),
    ]