from django.db import models


class Product(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_started = models.DateField()
    date_due = models.DateField()

    def __str__(self):
        return self.first_name
