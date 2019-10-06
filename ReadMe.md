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