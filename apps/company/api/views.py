from rest_framework import viewsets
from apps.company.models import Business
from apps.company.api.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = CompanySerializer