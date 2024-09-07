from django.db import models
from apps.ingredients.models import Ingredients
from apps.categories.models import Categories


class Plates(models.Model):
    name = models.CharField("Nombre", max_length=150)
    price = models.FloatField("Precio", default=0.0)
    ingredients = models.ManyToManyField(Ingredients, related_name="ingredients")
    category = models.ManyToManyField(Categories, related_name="category")
    image = models.ImageField("Imagen", upload_to="plates/")
    descriptions = models.TextField('Descripcion')

    def __str__(self):
        return self.name

    class Meta:
        """Meta definition for Products."""

        verbose_name = "Plate"
        verbose_name_plural = "Plates"
