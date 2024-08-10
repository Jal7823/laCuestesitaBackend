from rest_framework import serializers
from apps.drinks.models import Drinks

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'price', 'size', 'description', 'quantity']
