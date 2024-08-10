from rest_framework import viewsets
from apps.drinks.models import Drinks
from apps.drinks.api.serializers import DrinksSerializer

class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
