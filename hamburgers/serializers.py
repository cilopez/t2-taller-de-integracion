from rest_framework import serializers
from .models import Ingredient, Hamburger

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'url', 'nombre', 'descripcion')

class HamburgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburger
        fields = ('id', 'url', 'nombre', 'precio', 'descripcion', 'imagen','ingredientes')

class HamburgerPartialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburger
        fields = ('id', 'url', 'nombre', 'precio', 'descripcion', 'imagen')


