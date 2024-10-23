from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.categories.models import Categories

@admin.register(Categories)
class CategoriesAdmin(TranslatableAdmin):
    list_display = ('name',)

    # Configuración de los campos a mostrar en el admin
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
