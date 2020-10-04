from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'date_started',
        'date_due',
    )
    readonly_fields = ('pk',)


admin.site.register(Product, ProductAdmin)
