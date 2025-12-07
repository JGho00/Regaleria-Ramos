from django.db import models

#Clase categoria para clasificar los productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.nombre

#Clase producto que representa los productos en el sistema
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    vendedor = models.CharField(max_length=40, blank=True, null=True)
    #creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre