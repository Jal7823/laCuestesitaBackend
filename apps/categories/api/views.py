from rest_framework import viewsets
from apps.categories.models import Categories
from apps.categories.api.serializers import CategoriesSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
