### Material curs ORM django

Models i consultes per a realitzar amb django.


```
              +------------+
              |CATEGORIA   |
              +-----+------+
                    |
                    |
              +-----+------+
              |SUBCATEGORIA|
              +-----+------+
                    |
+-----+       +-----+------+          +-------+
|FLAG +-------+PRODUCTE    |      +---+FACTURA|
+-----+       +----------+-+      |   +-------+
                         |        |
                         |        |
                      +--+--------+----+
                      |LINIA DE FACTURA|
                      +----------------+

```

#### Inserció de dades inicials:

Entrar a la shell:

```
#activem venv
source ./venv/bin/activate
#entrem a la shell de django
python3 manage.py shell
```

#### Insertem dades inicials de productes:

```
from productes.models import Categoria, SubCategoria, Producte

# Categories
mascotes=Categoria.objects.create( nom="Mascotes" )
neteja,es_nou=Categoria.objects.get_or_create( nom="Neteja" )

if es_nou:
    print(f"{neteja.nom} s'ha creat de nou")


neteja,es_nou=Categoria.objects.get_or_create( nom="Neteja" )
if not es_nou:
    print(f"{neteja.nom} ja existia")


# Subcategories
gat=SubCategoria.objects.create(nom="Gats", categoria=mascotes)
gos=SubCategoria.objects.create(nom="Gos", categoria=mascotes)

cuina_i_bany=neteja.subcategoria_set.create(nom="Cuina i bany")
roba = neteja.subcategoria_set.create(nom="Roba")

# Productes
gat.producte_set.create(nom="Menjadora gat")
gat.producte_set.create(nom="Sorrera gat")

gos.producte_set.create(nom="Menjadora gos")
gos.producte_set.create(nom="Caseta gos")

cuina_i_bany.producte_set.create(nom="Renta plats")
roba.producte_set.create(nom="Sabó roba")
roba.producte_set.create(nom="Suavitzant")

# producte sense sub categoria
Producte.objects.create(nom="Pasta de dents")

```

Provem que no podem entrar repetits

```
from productes.models import Categoria, SubCategoria, Producte

# Categories
x=Categoria.objects.create( nom="x" )
Categoria.objects.create( nom="x" ) #django.db.utils.IntegrityError: UNIQUE constraint failed: productes_categoria.nom

# Dues subcategories amb el mateix nom dis la mateixa categoria
mascotes=Categoria.objects.get(nom="Mascotes")
y1=x.subcategoria_set.create(nom="y")
y2=mascotes.subcategoria_set.create(nom="y") # segona categoria amb nom "y" 
x.subcategoria_set.create(nom="y") # django.db.utils.IntegrityError: UNIQUE constraint failed: productes_subcategoria.nom, productes_subcategoria.categoria_id

# Eliminem dades de prova
for t in (x,y1,y2,):
    t.delete()
```

#### Insertem N:M

Insertem diferents flags i els assignem als productes:

```
from productes.models import Flags
drogeria = Flags.objects.create(nom="Drogueria")
nocaduca = Flags.objects.create(nom="Llarga Caducitat")
voluminos = Flags.objects.create(nom="Voluminós")

#Cerquem productes:
from productes.models import Producte
sabo=Producte.objects.get(nom__iexact="sabó roba")
menjadora=Producte.objects.filter(nom__startswith="Menjadora").first()


#Assignem flags a productes
sabo.flags.add(drogeria)
sabo.flags.all() #comprovem

menjadora.flags.set([nocaduca,voluminos])
nocaduca.producte_set.all() #comprovem, aquest cop, des del flag cap al producte
```

### Consultes bàsiques

* Tots els productes: `Producte.objects.all()`
* Tots els productes que continguin la lletra "o": `Producte.objects.filter(nom__icontains="o")`
* Totes les subcategories modificades fa més de 1 minut:

```
from datetime import datetime, timedelta
from productes.models import SubCategoria
from django.utils.timezone import get_current_timezone

# en modifico una ara
subcategoria_gos=SubCategoria.objects.get(nom="Gos")
subcategoria_gos.darrera_modificacio
subcategoria_gos.nom="Gos"
subcategoria_gos.save()
subcategoria_gos.darrera_modificacio # comprovem que ha canviat

fa_un_minut = datetime.now(tz=get_current_timezone()) - timedelta(minutes=1)  # or Naive
SubCategoria.objects.filter(darrera_modificacio__lte=fa_un_minut) # comprovem que no surt la subcategoria gos.
```

* Tots els productes de la categoria "Mascotes":

```
from productes.models import Producte
Producte.objects.filter(sub_categoria__categoria__nom__iexact = "mascotes" )

#naturalment també es pot fer:
from productes.models import Categoria
mascotes = Categoria.objects.get(nom__iexact="mascotes")
Producte.objects.filter(sub_categoria__categoria = mascotes )
```

* Tots els productes amb el flag "Drogeria": `Producte.objects.filter( flags__nom="Drogueria")`


