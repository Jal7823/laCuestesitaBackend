from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Business(TranslatableModel): 
    # Translatable fields
    translations = TranslatedFields(
        name=models.CharField(max_length=255)
    )

    # Basic information
    tax_id = models.CharField(max_length=50, unique=True)  
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)

    # Business details
    opening_hours = models.JSONField(blank=True, null=True)  # Stores opening hours by day
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Path to the logo image
    registration_date = models.DateField(auto_now_add=True)
    business_type = models.CharField(max_length=50, choices=[('restaurant', 'Restaurant'), ('bar', 'Bar'), ('cafe', 'Cafe')])

    # Billing information
    bank_account = models.CharField(max_length=100, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    payment_terms = models.CharField(max_length=50, blank=True, null=True)

    # Additional information
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
