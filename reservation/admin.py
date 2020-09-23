from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ('reservation_number', 'first_name','room',
                       'check_in', 'check_out',
                       'adults', 'children',
                       'specials', 'nights',
                       'total_cost',)

    fields = ('reservation_number', 'first_name',
              'check_in', 'check_out',
              'adults', 'children',
              'specials', 'nights',
              'date_posted', 'user',
              'email', 'total_cost',)

    list_display = ('reservation_number', 'date_posted',
                    'first_name', 'check_in',
                    'check_out', 'total_cost',)


admin.site.register(Reservation, ReservationAdmin)
