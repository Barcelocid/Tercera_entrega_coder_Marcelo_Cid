from django.db import models

# Create your models here.

class pais(models.Model):
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.pais} {self.ciudad}"

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.rut}"

class comida(models.Model):
    fondo = models.CharField(max_length=50)
    bebida = models.CharField(max_length=50)
    postre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.fondo} {self.bebida} {self.postre}"
    