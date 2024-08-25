from rest_framework import serializers
from apps.plates.models import Plates
from apps.ingredients.api.serializers import IngredientsSerializer
from apps.categories.api.serializers import CategoriesSerializer

class PlatesSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)
    category = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Plates
        fields = ['id', 'name', 'price', 'ingredients', 'category', 'image']
  