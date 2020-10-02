from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Room, Booking
from django.views.generic import (
    ListView,
    FormView,
    DetailView,
    UpdateView,
    DeleteView
)
from .forms import CheckRoomsForm
from hotel.booking_functions.availability import check_availability


class Gallery(ListView):
    model = Room
    template_name = "gallery.html"


class RoomList(ListView):
    model = Room
    template_name = 'rooms.html'


class BookingList(ListView): 
    model = Booking
    template_name = 'bookings.html'


class BookingView(FormView):
    form_class = CheckRoomsForm
    template_name = 'reservation_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                user = self.request.user,
                room = room,
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


class BookingDetailsView(DetailView):
    model = Booking
    template_name = "booking_detail.html"


class BookingUpdateView(UpdateView):
    model = Booking
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


class BookingDeleteView(DeleteView):
    model = Booking
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
