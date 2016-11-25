# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='tiendas/imagen/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=15)),
                ('foto', models.ImageField(upload_to='tiendas/imagen/', blank=True, null=True)),
                ('productos', models.ManyToManyField(to='tiendas.Producto', through='tiendas.Inventario')),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(to='tiendas.Producto'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='tienda',
            field=models.ForeignKey(to='tiendas.Tienda'),
        ),
    ]
