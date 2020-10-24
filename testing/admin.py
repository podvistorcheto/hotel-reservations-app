from django.contrib import admin
from .models import Unit, Reservation

# Register your models here.


class UnitAdmin(admin.ModelAdmin):
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


class ReservationAdmin(admin.ModelAdmin):
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

admin.site.register(Unit, UnitAdmin)
admin.site.register(Reservation,ReservationAdmin)
