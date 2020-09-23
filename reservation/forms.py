from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('reservation_number', 'first_name',
                  'check_in', 'check_out',
                  'adults', 'children',
                  'specials', 'nights',
                  'date_posted', 'user',
                  'email',)
