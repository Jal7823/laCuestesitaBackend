from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Ingredients(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        descriptions=models.TextField(blank=True, null=True)  # Si quieres agregar descripción o más campos
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
