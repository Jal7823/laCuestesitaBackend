from rest_framework import viewsets, filters
from apps.plates.models import Plates
from apps.plates.api.serializers import PlatesSerializer
from apps.users.permisionsUsers import IsBoss

class PlatesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Plates instances.
    Allows filtering by category name.
    """
    queryset = Plates.objects.all()
    serializer_class = PlatesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__translations__name']  # Cambiado para manejar traducciones
    # permission_classes = [IsBoss]

    def get_queryset(self):
        """
        Optionally filters the plates by category name.
        """
        queryset = super().get_queryset()
        term = self.request.query_params.get('category', None)
        if term:
            # Filtrar por el nombre de la categoría en las traducciones
            queryset = queryset.filter(category__translations__name__icontains=term)
        return queryset
