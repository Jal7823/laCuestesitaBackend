from rest_framework import viewsets, filters
from apps.plates.models import Plates
from apps.plates.api.serializers import PlatesSerializer

class PlatesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Plates instances.
    Allows filtering by category name.
    """
    queryset = Plates.objects.all()
    serializer_class = PlatesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name'] 

    def get_queryset(self):
        """
        Optionally filters the plates by category name.
        """
        queryset = super().get_queryset()
        term = self.request.query_params.get('category', None)
        print(term)
        if term:
            queryset = queryset.filter(category__name__icontains=term)
        return queryset
