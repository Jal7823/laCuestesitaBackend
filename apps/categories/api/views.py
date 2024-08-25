from rest_framework.response import Response
from rest_framework import viewsets
from apps.categories.models import Categories
from apps.categories.api.serializers import CategoriesSerializer
from drf_spectacular.utils import extend_schema_view,extend_schema


@extend_schema_view(
    list=extend_schema(
        tags=['Categories'],
        description='Should get all Categories'
    ),
    create=extend_schema(
        tags=['Categories'],
        description='Create a new instance of Categories',
        request=CategoriesSerializer,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    retrieve=extend_schema(
        tags=['Categories'],
        description='Retrieve a specific instance of Categories by ID',
        responses={
            200: CategoriesSerializer,
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    update=extend_schema(
        tags=['Categories'],
        description='Update a specific instance of Categories by ID',
        request=CategoriesSerializer,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    partial_update=extend_schema(
        tags=['Categories'],
        description='Partial update a specific instance of Categories by ID',
        request=CategoriesSerializer,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    destroy=extend_schema(
        tags=['Categories'],
        description='Delete a specific instance of Categories by ID',
    ),
)
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

