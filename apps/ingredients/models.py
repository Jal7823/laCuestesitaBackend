from django.db import models

class Ingredients(models.Model):
    name = models.CharField('Nombre', max_length=50)
    price = models.FloatField('Precio',default=0.0,null=True,blank=True)