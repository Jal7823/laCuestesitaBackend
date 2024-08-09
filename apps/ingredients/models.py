from django.db import models

class Ingredients(models.Model):
    name = models.CharField('Nombre', max_length=50)
    price = models.FloatField('Precio',default=0.0,null=True,blank=True)


#TODO YOU NEED FINISH THE MODEL
    def __str__(self):
        return {self.name}

    class Meta:
        """Meta definition for Products."""

        verbose_name = 'Drinks'
        verbose_name_plural = 'Drinks'