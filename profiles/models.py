from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.

class LocalUser(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    to create or modify the local user profile
    """
    if created:
        LocalUser.objects.create(user=instance)
    # or save the profile if its user exists already
    instance.localuser.save()