from rest_framework import viewsets
from apps.ingredients.models import Ingredients
from apps.ingredients.api.serializers import IngredientsSerializer

class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
