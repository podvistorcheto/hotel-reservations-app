from django import forms
from django.utils import timezone


class CheckRoomsForm(forms.Form):
    UNIT_CATEGORIES = (
        ('twin', 'Villa Bor'),
        ('dbl', 'Vila Ela'),
        ('fam', 'Villa Arka'),
        ('dsui', 'Villa Aspen'),
        ('apt', 'Villa Iris'),
        ('dapt', 'Villa Alagen'),
    )
    unit_category = forms.ChoiceField(
        choices=UNIT_CATEGORIES, required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    adults = forms.IntegerField()
    children = forms.IntegerField()
    check_in = forms.DateTimeField()
    check_out = forms.DateTimeField()
    specials = forms.CharField(
        label='Special Request', max_length=250, required=False)

