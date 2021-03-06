from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.conf import settings
from profiles.models import CreateProfile


class Unit(models.Model):
    UNIT_CATEGORIES = (
        ('twin', 'Villa Bor'),
        ('dbl', 'Vila Ela'),
        ('fam', 'Villa Arka'),
        ('dsui', 'Villa Aspen'),
        ('apt', 'Villa Iris'),
        ('dapt', 'Villa Alagen'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=25, choices=UNIT_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    children_capacity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.category}'


class Reservation(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Unit, on_delete=models.CASCADE)
    adults = models.IntegerField(null=False)
    children = models.IntegerField(null=True)
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    specials = models.TextField(
        max_length=256, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f'Booked {self.room} from {self.check_in} to {self.check_out}'

    def get_absolute_url(self):
        return reverse("booking-details", kwargs={"pk": self.pk})
