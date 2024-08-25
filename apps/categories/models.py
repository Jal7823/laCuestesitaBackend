from django.db import models

class Categories(models.Model):
    name = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        """Meta definition for Products."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
