# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-03-10 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=70)),
                ('descripcion', models.CharField(max_length=250)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('estado', models.CharField(choices=[('Abierto', 'Abierto'), ('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Resuelto', 'Resuelto'), ('Cerrado', 'Cerrado')], max_length=15)),
            ],
        ),
    ]
