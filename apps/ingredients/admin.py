from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Ingredients

@admin.register(Ingredients)
class IngredientsAdmin(TranslatableAdmin):
    list_display = ('name', 'price')

    # Esto permitirá que los campos traducibles aparezcan en el admin
    fieldsets = (
        (None, {
            'fields': ('name', 'price')
        }),
    )
