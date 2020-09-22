from django import forms
from django.utils import timezone


class CheckRoomsForm(forms.Form):
    ROOM_CATEGORIES = (
        ('twin', 'Twin Room'),
        ('dbl', 'Double Room'),
        ('fam', 'Family Room'),
        ('dsui', 'Deluxe Suite'),
        ('apt', 'Apartment'),
        ('dapt', 'Deluxe Apartment'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    adults = forms.IntegerField()
    children = forms.IntegerField()
    check_in = forms.DateTimeField()
    check_out = forms.DateTimeField()
    specials = forms.CharField(label='Special Request', max_length=100)
