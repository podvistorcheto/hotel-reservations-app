from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ReservationForm


def make_reservation(request):
    booking = request.session.get('booking', {})
    if not booking:
        messages.error(request, "There is nothing in your bag at the moment")
    return redirect('room-list')

    order_form = ReservationForm()
    template = 'reservation.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)