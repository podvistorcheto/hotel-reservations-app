from django.contrib import admin
from .models import Room, Booking

# Register your models here.
from django.contrib import admin
from .models import Room, Booking


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'category',
        'beds',
        'capacity',
        'children_capacity',
        'price',
    )
    readonly_fields = ('pk',)

    ordering = ('number',)


class BookingAdmin(admin.ModelAdmin):
    list_display = (
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
    readonly_fields = ('pk', 'date_posted')

    ordering = ('date_posted',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking,BookingAdmin)