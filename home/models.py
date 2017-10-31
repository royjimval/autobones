# -*- coding: utf-8 -*- pendejo
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=30)

class Modelo(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca) #Trae datos de la tabla de Marca

class Carro(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca) #Trae datos de la tabla de marca
    modelo = models.ForeignKey(Modelo) #Trae datos de la tabla de modelos

#====================================================
#Modelos de tipos de partes
#====================================================

Motores = (("4","4"),("6","6"),("8","8"))
Transmision = (("Manual","Manual"),("Automatica","Automatica"))
Categoria = (("Electricas","Electricas"),("Mecanicas","Mecanicas"),("Carroceria","Carroceria"))

class Partes_maestro(models.Model):
    categoria = models.CharField(max_length= 30, choices = Categoria)

class Partes_electricas(models.Model):
    parte = models.OneToOneField(Partes_maestro, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=30)
    carro = models.ForeignKey(Carro) #Trae datos de la tabla de carro

class Partes_mecanicas(models.Model):
    parte = models.OneToOneField(Partes_maestro, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=30)
    motor = models.CharField(max_length= 30, choices = Motores)
    transmision = models.CharField(max_length= 30, choices = Transmision)
    carro = models.ForeignKey(Carro) #Trae datos de la tabla de carro

class Partes_carroceria(models.Model):
    parte = models.OneToOneField(Partes_maestro, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=30)
    carro = models.ForeignKey(Carro) #Trae datos de la tabla de carro
    color = models.CharField(max_length=30)
    nivel_m = models.IntegerField()


class Sucursal(models.Models):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)


class Inventario(models.Model):
    cantitad = models.IntegerField()
    costo = models.IntegerField()
    origen_sucursal = models.ForeignKey(Sucursal)
    catalogo = models.ForeignKey(Catalogo)

#Delete "inventario"
