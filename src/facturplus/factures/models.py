from django.db import models

class LiniaFactura(models.Model):
    quantitat = models.IntegerField()
    preu_unitari = models.DecimalField(max_digits=8, decimal_places=2)
    factura = models.ForeignKey("Factura", on_delete=models.PROTECT)
    producte = models.ForeignKey("productes.Producte", on_delete=models.PROTECT)


class Factura(models.Model):
    descripcio = models.CharField(max_length=50)
    data_factura = models.DateTimeField()
    nom_client = models.CharField(max_length=150)
    productes = models.ManyToManyField("productes.Producte", through=LiniaFactura)
    
