from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from profiles.models import CreateProfile


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('twin', 'Twin Room'),
        ('dbl', 'Double Room'),
        ('fam', 'Family Room'),
        ('dsui', 'Deluxe Suite'),
        ('apt', 'Apartment'),
        ('dapt', 'Deluxe Apartment'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=25, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    children_capacity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.category}'


class Booking(models.Model):
    user_profile = models.ForeignKey(
        CreateProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    adults = models.IntegerField(null=False)
    children = models.IntegerField(null=True)
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    specials = models.TextField(
        max_length=256, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} booked {self.room} from {self.check_in} to {self.check_out}'

    def get_absolute_url(self):
        return reverse("booking-details", kwargs={"pk": self.pk})
