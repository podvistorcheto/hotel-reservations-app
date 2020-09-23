import uuid
from django.utils import timezone
from django.db import models
from django.conf import settings
from hotel.models import Room, Booking


class Reservation(models.Model):

    reservation_number = models.CharField(max_length=32, null=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    user = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    adults = models.IntegerField(null=False, blank=False, default=0)
    children = models.IntegerField(null=True, blank=False, default=0)
    check_in = models.DateTimeField(null=False, blank=False)
    check_out = models.DateTimeField(null=False, blank=False)
    nights = models.DecimalField(max_digits=30, decimal_places=2, null=False, blank=False, default=0)
    specials = models.TextField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2,null=False, default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    def _generate_rsv_number(self):
        """
        generate unique reservation number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        overrides primary save() to set unique
        order number
        """
        if not self.order_number:
            self._order_number = self._generate_rsv_number()
        super().save(*args, **kwargs)

    def __str_(self):
        return self.order.number
