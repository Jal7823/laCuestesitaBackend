from django.db import models

class Drinks(models.Model):
    name = models.CharField('Nombre', max_length=50)
    price = models.FloatField('Precio',default=0.0,null=True,blank=True)
    size= models.IntegerField('Tamagno',default=0,null=True,blank=True)
    description = models.TextField('Descricion',null=True,blank=True)
    quantity = models.IntegerField('Cantidad',default=0,null=True,blank=True)

    def __str__(self):
        return {self.name}

    class Meta:
        """Meta definition for Products."""

        verbose_name = 'Drinks'
        verbose_name_plural = 'Drinks'