from rest_framework import serializers
from apps.ingredients.models import Ingredients
from parler_rest.serializers import TranslatableModelSerializer
from django.utils.translation import get_language

class IngredientsSerializer(TranslatableModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        current_language = get_language()

        if 'translations' in representation and current_language in representation['translations']:
            translation = representation['translations'][current_language]
            representation.update(translation)

        representation.pop('translations', None)

        return representation

    class Meta:
        model = Ingredients
        fields = ['id', 'name', 'price', 'translations']
