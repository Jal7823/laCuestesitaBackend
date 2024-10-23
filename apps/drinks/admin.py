from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.drinks.models import Drinks

@admin.register(Drinks)
class DrinksAdmin(TranslatableAdmin):
    list_display = ('name', 'price')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'size', 'quantity', 'image')
        }),
    )
