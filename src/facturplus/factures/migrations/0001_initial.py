# Generated by Django 2.2.6 on 2019-10-06 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcio', models.CharField(max_length=50)),
                ('data_factura', models.DateTimeField()),
                ('nom_client', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LiniaFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitat', models.IntegerField()),
                ('preu_unitari', models.DecimalField(decimal_places=2, max_digits=8)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='factures.Factura')),
                ('producte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productes.Producte')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='productes',
            field=models.ManyToManyField(through='factures.LiniaFactura', to='productes.Producte'),
        ),
    ]
