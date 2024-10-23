from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Drinks(TranslatableModel):  # Extiende de TranslatableModel
    translations = TranslatedFields(
        name=models.CharField('Nombre', max_length=50),  # Solo en TranslatedFields
        description=models.TextField('Descripción', null=True, blank=True)  # Descripción traducible
    )
    price = models.FloatField('Precio', default=0.0, null=True, blank=True)
    size = models.IntegerField('Tamaño', default=0, null=True, blank=True)
    quantity = models.IntegerField('Cantidad', default=0, null=True, blank=True)
    image = models.ImageField('Imagen', upload_to='drinks/')

    class Meta:
        verbose_name = 'Drink'
        verbose_name_plural = 'Drinks'

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
