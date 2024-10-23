from rest_framework import serializers
from apps.plates.models import Plates
from apps.ingredients.api.serializers import IngredientsSerializer
from apps.categories.api.serializers import CategoriesSerializer
from parler_rest.serializers import TranslatableModelSerializer
from django.utils.translation import get_language

class PlatesSerializer(TranslatableModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)
    category = CategoriesSerializer(many=True, read_only=True)

    # Sobrescribir el método 'to_representation' para filtrar las traducciones
    def to_representation(self, instance):
        # Obtener la representación original
        representation = super().to_representation(instance)

        # Obtener el idioma actual de la solicitud
        current_language = get_language()

        # Si hay traducciones y el idioma actual está presente
        if 'translations' in representation and current_language in representation['translations']:
            translation = representation['translations'][current_language]
            # Sobrescribir los campos con las traducciones específicas del idioma
            representation.update(translation)

        # Remover el campo translations de la respuesta final
        representation.pop('translations', None)

        return representation

    class Meta:
        model = Plates
        # Asegurarse de incluir el campo 'descriptions' en los campos del serializador
        fields = ['id', 'name', 'price', 'ingredients', 'category', 'image', 'descriptions', 'translations']
