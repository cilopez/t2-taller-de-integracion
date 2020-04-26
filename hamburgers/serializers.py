from rest_framework import serializers
from .models import Ingredient, Hamburger

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'url', 'name', 'description')

class HamburgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburger
        fields = ('id', 'url', 'name', 'price', 'description', 'image','ingredients')

class HamburgerPartialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburger
        fields = ('id', 'url', 'name', 'price', 'description', 'image')


