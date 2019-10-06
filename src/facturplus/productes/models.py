from django.db import models

class Categoria(models.Model):
    nom = models.CharField(max_length=50, unique=True )
    moment_alta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class SubCategoria(models.Model):
    nom = models.CharField(max_length=50)
    categoria = models.ForeignKey( Categoria, on_delete=models.CASCADE )
    darrera_modificacio = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.categoria.nom} > {self.nom}"

    class Meta:
        unique_together = [['nom', 'categoria']]

class Flags(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Producte(models.Model):
    nom = models.CharField(max_length=50)
    sub_categoria = models.ForeignKey( SubCategoria, blank=True, null=True, on_delete=models.SET_NULL )
    flags = models.ManyToManyField(Flags)

    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ["sub_categoria__categoria__nom", "sub_categoria__nom", "nom"]



