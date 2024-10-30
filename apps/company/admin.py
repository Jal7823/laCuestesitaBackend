from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Business

@admin.register(Business)
class BusinessAdmin(TranslatableAdmin):
    list_display = ('name', 'tax_id', 'email', 'phone_number', 'status', 'registration_date')
    search_fields = ('translations__name', 'tax_id', 'email')
    list_filter = ('status', 'business_type', 'registration_date', 'country')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tax_id', 'address', 'city', 'state', 'country', 'postal_code', 'phone_number', 'email', 'website')
        }),
        ('Business Details', {
            'fields': ('opening_hours', 'logo', 'business_type')
        }),
        ('Billing Information', {
            'fields': ('bank_account', 'billing_address', 'payment_terms')
        }),
        ('Additional Information', {
            'fields': ('status', 'notes')
        }),
    )

    list_editable = ('status', 'phone_number')
