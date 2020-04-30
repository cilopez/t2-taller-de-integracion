from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets,status
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
        if Hamburger.objects.filter(id=self.kwargs['hamburguesa_pk']).exists():
            hamburger = Hamburger.objects.get(pk=self.kwargs['hamburguesa_pk'])
            query = Ingredient.objects.filter(ingredients__in=[self.kwargs['hamburguesa_pk']])
            return query
        return Ingredient.objects.none()

    def destroy(self, request, *args, **kwargs):
        if Hamburger.objects.filter(id=self.kwargs['hamburguesa_pk']).exists():
            hamburger = Hamburger.objects.get(pk=self.kwargs['hamburguesa_pk'])
            ingredient = self.get_object()
            hamburger.ingredientes.remove(ingredient)
            return Response(status=200, data='Ingrediente retirado')
        return Response(status=400, data='Id de hamburguesa inválido')


    def update(self, request, *args, **kwargs):
        if Hamburger.objects.filter(id=self.kwargs['hamburguesa_pk']).exists():
            hamburger = Hamburger.objects.get(pk=self.kwargs['hamburguesa_pk'])
            if Ingredient.objects.filter(pk=self.kwargs['pk']).exists():
                ingredient = Ingredient.objects.get(pk=self.kwargs['pk'])
                hamburger.ingredientes.add(ingredient)
                return Response(status=201,data='Ingrediente agregado')
            return Response(status=404, data='Ingrediente inexistente')
        return Response(status=400, data='Id de hamburguesa inválido')



class IngredientView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def destroy(self, request, *args, **kwargs):
        ingredient = self.get_object()
        for x in Hamburger.objects.all():
            if ingredient in x.ingredientes.all():
                return Response(status=409,data='Ingrediente no se puede borrar, se encuentra presente en una hamburguesa')
        ingredient.delete()
        return Response(status=200,data='Ingrediente eliminado')
    
    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        serializer_ingredient = IngredientSerializer(data=request.data,context=serializer_context)
        if serializer_ingredient.is_valid():
            try:
                serializer_ingredient.save()
                return Response(status=201,data=serializer_ingredient.data)
            except Exception as err:
                return Response(status=400,data='Input invalido')
        return Response(status=400,data='Input invalido')


class HamburgerView(viewsets.ModelViewSet):
    queryset = Hamburger.objects.all()
    http_method_names = ['get', 'post', 'delete', 'patch']
    
    def get_serializer_class(self):
        if self.action == "partial_update":
             return HamburgerPartialSerializer
        return HamburgerSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        serializer_burger = HamburgerSerializer(data=request.data,context=serializer_context)
        if serializer_burger.is_valid():
            try:
                serializer_burger.save()
                return Response(status=201,data=serializer_burger.data)
            except Exception as err:
                return Response(status=400,data='Input invalido')
        return Response(status=400,data='Input invalido')
    
    def destroy(self, request, *args, **kwargs):
        hamburger = self.get_object()
        hamburger.delete()
        return Response(status=200,data='Hamburguesa eliminada')






