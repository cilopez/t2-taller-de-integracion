from django.db import models


class Ingredient(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=512)

    def __str__(self):
        return self.nombre


class Hamburger(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=512)
    imagen = models.CharField(max_length=512)
    ingredientes = models.ManyToManyField(Ingredient,related_name='ingredients', null=True, blank=True)

    
    def __str__(self):
        return self.nombre