from rest_framework import serializers
from apps.company.models import Business
from parler_rest.serializers import TranslatableModelSerializer
from django.utils.translation import get_language

class CompanySerializer(TranslatableModelSerializer):
    def to_representation(self, instance):
        # Get the base representation
        representation = super().to_representation(instance)
        current_language = get_language()  # Get the current language

        # Extract and update translations in the current language, if available
        if 'translations' in representation and current_language in representation['translations']:
            translation = representation['translations'][current_language]
            representation.update(translation)

        # Remove translations field from the final output
        representation.pop('translations', None)

        return representation

    class Meta:
        model = Business
        fields = [
            'id', 'name', 'tax_id', 'address', 'city', 'state', 'country', 
            'postal_code', 'phone_number', 'email', 'website', 'opening_hours', 
            'logo', 'registration_date', 'business_type', 'bank_account', 
            'billing_address', 'payment_terms', 'status', 'notes', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at'] 
