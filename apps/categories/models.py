from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Categories(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField('Nombre', max_length=100)
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
