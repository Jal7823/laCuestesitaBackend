from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Plates

@admin.register(Plates)
class PlatesAdmin(TranslatableAdmin):
    list_display = ('name', 'price')

    # Esto permitirá que los campos traducibles aparezcan en el admin
    fieldsets = (
        (None, {
            'fields': ('name', 'descriptions', 'price', 'ingredients', 'category', 'image')
        }),
    )
