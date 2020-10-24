from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Unit, Reservation
from django.views.generic import (
    ListView,
    FormView,
    DetailView,
    UpdateView,
    DeleteView,
    View
)
from .forms import CheckRoomsForm


class Pics(ListView):
    model = Unit
    template_name = "gallery.html"


class UnitsListView(ListView):
    model = Unit
    template_name = 'rooms.html'


class UnitsDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = CheckRoomsForm()
        unit_list = Unit.objects.filter(category=category)

        if len(unit_list) > 0:
            unit = unit_list[0]
            unit_category = dict(unit.UNIT_CATEGORIES).get(unit.category, None)
            context = {
                'unit_category': unit_category,
                'form': form,
            }
            return render(request, 'test_form.html', context)


class RsvsList(ListView):
    model = Reservation
    template_name = 'bookings.html'


class RsvsView(FormView):
    form_class = CheckRoomsForm
    template_name = 'reservation_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        unit_list = Unit.objects.filter(category=data['unit_category'])
        available_rooms = []
        for unit in unit_list:
            if check_availability(unit, data['check_in'], data['check_out']):
                available_rooms.append(unit)
        if len(available_rooms)>0:
            unit = available_rooms[0]
            booking = Booking.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                user = self.request.user,
                unit = unit,
                adults = data['adults'],
                children = data['children'],
                check_in = data['check_in'],
                check_out = data['check_out'],
                specials = data['specials'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse(
                'These rooms are booked the dates you are looking for.')


class RsvsDetailsView(DetailView):
    model = Reservation
    template_name = "booking_detail.html"


class RsvsUpdateView(UpdateView):
    model = Reservation
    template_name = "reservation_form.html"
    fields = (
        'first_name',
        'last_name',
        'user',
        'room',
        'adults',
        'children',
        'check_in',
        'check_out',
        'specials',
        )

    def update_form(self, pk):
        booking = Booking.objects.get(id=pk)
        form = CheckRoomsForm(instance=booking)
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.update(
                first_name = data['first_name'],
                last_name = data['last_name'],
                user = self.request.user,
                room = room,
                adults = data['adults'],
                children = data['children'],
                check_in = data['check_in'],
                check_out = data['check_out'],
                specials = data['specials'], # should look for option to auto_add modified at: dd/mm/yyyy
            )
            booking.save()
            return reverse(self, "booking-details", kwargs={"pk": self.pk})
        else:
            return HttpResponse(
                'These rooms are booked the dates you are looking for.')


class RsvsDeleteView(DeleteView):
    model = Reservation
    template_name = "booking_delete.html"
    success_url = reverse_lazy('bookings')
    fields = (
        'first_name',
        'last_name',
        'user',
        'room',
        'adults',
        'children',
        'check_in',
        'check_out',
        'specials',
        )

    def delete_booking(self, form, pk):
        booking = Booking.objects.get(id=pk)
        form = CheckRoomsForm(instance=booking)
        if form.method == "POST":
            booking = Booking.objects.delete(
                first_name = data['first_name'],
                last_name = data['last_name'],
                user = self.request.user,
                room = room,
                adults = data['adults'],
                children = data['children'],
                check_in = data['check_in'],
                check_out = data['check_out'],
                specials = data['specials'], # should look for option to auto_add modified at: dd/mm/yyyy
            )
            booking.delete()
            return HttpResponse('Reservation cancelled successfully')
