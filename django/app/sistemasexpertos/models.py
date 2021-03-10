# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
import datetime
from django.utils import timezone
OPCIONES_ESTADO = (
    ('Abierto', 'Abierto'),
    ('Pendiente', 'Pendiente'),
    ('En Proceso', 'En Proceso'),
    ('Resuelto', 'Resuelto'),
    ('Cerrado', 'Cerrado'),
)
# Create your models here.
class Ticket(models.Model):
    id   = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=250)
    datetime = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    estado = models.CharField(choices=OPCIONES_ESTADO, max_length=15)

class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('id','datetime','creado_hace',)
    fields = ('id','titulo','descripcion','datetime','estado','creado_hace',)
    list_display = ('estado', 'creado_hace', 'id', 'titulo', 'descripcion','datetime')
    search_fields = ('id','titulo','descripcion','datetime','estado')
    list_filter = ['estado'] 
    def creado_hace(self, obj):
        try:
            return timezone.localtime() - obj.datetime
        except:
            return 0
