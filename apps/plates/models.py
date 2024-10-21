from django.db import models
from apps.ingredients.models import Ingredients
from apps.categories.models import Categories
from parler.models import TranslatableModel, TranslatedFields

class Plates(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField("Nombre", max_length=150),
        descriptions=models.TextField('Descripcion'),
    )
    price = models.FloatField("Precio", default=0.0)
    ingredients = models.ManyToManyField(Ingredients, related_name="ingredients")
    category = models.ManyToManyField(Categories, related_name="category")
    image = models.ImageField("Imagen", upload_to="plates/")

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)or "Unnamed Plate"

    class Meta:
        verbose_name = "Plate"
        verbose_name_plural = "Plates"
