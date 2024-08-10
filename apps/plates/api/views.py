from rest_framework import viewsets
from apps.plates.models import Plates
from apps.plates.api.serializers import PlatesSerializer
from rest_framework import filters

class PlatesViewSet(viewsets.ModelViewSet):
    queryset = Plates.objects.all()
    serializer_class = PlatesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']  # Permite buscar Plates por categoría
