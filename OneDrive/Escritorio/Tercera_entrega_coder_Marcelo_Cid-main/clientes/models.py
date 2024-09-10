from django.db import models


# Se crea la clase/modelo pais con los atributos de cada una de ellas
class pais(models.Model):
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.pais} {self.ciudad}"

# Se crea la clase/modelo cliente con los atributos de cada una de ellas
class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.rut}"

# Se crea la clase/modelo comida con los atributos de cada una de ellas
class comida(models.Model):
    fondo = models.CharField(max_length=50)
    bebida = models.CharField(max_length=50)
    postre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.fondo} {self.bebida} {self.postre}"
    