from django.db import models

class Categoria(models.Model):
    nom = models.CharField(max_length=50)
    moment_alta = models.DateTimeField(auto_now_add=True)

class SubCategoria(models.Model):
    nom = models.CharField(max_length=50)
    categoria = models.ForeignKey( Categoria, on_delete=models.CASCADE )
    darrera_modificacio = models.DateTimeField(auto_now=True)

class Flags(models.Model):
    nom = models.CharField(max_length=50)

class Producte(models.Model):
    nom = models.CharField(max_length=50)
    sub_categoria = models.ForeignKey( SubCategoria, blank=True, null=True, on_delete=models.SET_NULL )
    flags = models.ManyToManyField(Flags)

    




