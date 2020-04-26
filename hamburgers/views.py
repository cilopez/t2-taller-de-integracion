from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingredient, Hamburger
from .serializers import IngredientSerializer, HamburgerSerializer, HamburgerPartialSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.core import serializers
import json

class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    http_method_names = ['get','delete', 'put']

    def get_queryset(self):
        return Ingredient.objects.filter(ingredients__in=[self.kwargs['hamburguesa_pk']])

    def destroy(self, request, *args, **kwargs):
        hamburger = Hamburger.objects.get(pk=self.kwargs['hamburguesa_pk'])
        ingredient = self.get_object()
        hamburger.ingredients.remove(ingredient)
        return Response(data='Delete success')
    
    # def partial_update(self, request, *args, **kwargs):
    #     print('hola')
    #     # hamburger = Hamburger.objects.get(pk=self.kwargs['hamburguesa_pk'])
    #     # ingredient = self.get_object()
    #     # hamburger.ingredients.add(ingredient)
    #     # return Response(data='New ingredient added to burger')


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def destroy(self, request, *args, **kwargs):
        ingredient = self.get_object()
        for x in Hamburger.objects.all():
            if ingredient in x.ingredients.all():
                return Response(data='Delete Denied: Ingredient is part of a existing hamburger')
        ingredient.delete()
        return Response(data='Delete success')


class HamburgerView(viewsets.ModelViewSet):
    queryset = Hamburger.objects.all()
    http_method_names = ['get', 'post', 'delete', 'patch']
    
    def get_serializer_class(self):
        if self.action == "partial_update":
             return HamburgerPartialSerializer
        return HamburgerSerializer

