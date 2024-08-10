from django.db import models

class Ingredients(models.Model):
    name = models.CharField('Nombre', max_length=50)
    price = models.FloatField('Precio', default=0.0, null=True, blank=True)

    def __str__(self):
        return self.name  # Aquí devolvemos self.name como cadena

    class Meta:
        """Meta definition for Products."""
        verbose_name = 'Ingredient'  # Singular para verbose_name
        verbose_name_plural = 'Ingredients'
