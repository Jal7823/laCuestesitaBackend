from django.db import models

class Drinks(models.Model):  # Renamed class to singular 'Drink'
    name = models.CharField('Nombre', max_length=50)
    price = models.FloatField('Precio', default=0.0, null=True, blank=True)
    size = models.IntegerField('Tamaño', default=0, null=True, blank=True)  # Corrected spelling of 'Tamaño'
    description = models.TextField('Descripción', null=True, blank=True)  # Corrected spelling of 'Descripción'
    quantity = models.IntegerField('Cantidad', default=0, null=True, blank=True)
    image = models.ImageField('Imagen', upload_to='drinks/')

    class Meta:
        """Meta definition for Drink."""
        verbose_name = 'Drink'  # Corrected to represent the model name
        verbose_name_plural = 'Drinks'

    def __str__(self):
        """Unicode representation of Drink."""
        return self.name
