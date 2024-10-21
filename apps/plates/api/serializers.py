from rest_framework import serializers
from apps.plates.models import Plates
from apps.ingredients.api.serializers import IngredientsSerializer
from apps.categories.api.serializers import CategoriesSerializer
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

class PlatesSerializer(TranslatableModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)
    category = CategoriesSerializer(many=True, read_only=True)
    translations = TranslatedFieldsField(shared_model=Plates)  # Aquí agregas las traducciones

    class Meta:
        model = Plates
        fields = ['id', 'name', 'price', 'ingredients', 'category', 'image', 'translations']
