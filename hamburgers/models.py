from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Hamburger(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=512)
    image = models.CharField(max_length=512)
    ingredients = models.ManyToManyField(Ingredient,related_name='ingredients', null=True, blank=True)

    
    def __str__(self):
        return self.name