from django.contrib import admin
from .models import Room, Booking


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'category',
        'beds',
        'capacity',
        'children_capacity',
    )

    ordering = ('number',)


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'category',
        'beds',
        'capacity',
        'children_capacity',
    )

    ordering = ('number',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking)
