# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import generics
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TicketList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer
    def get_queryset(self):
        queryset = Ticket.objects.all().order_by('pk')
        id = self.request.query_params.get('id', None)
        palabra = self.request.query_params.get('palabra', None)
        estado = self.request.query_params.get('estado', None)
        if id is not None:
            queryset = queryset.filter(id__icontains=id)
        if palabra is not None:
            queryset = queryset.filter(Q(descripcion__icontains=palabra) | Q(titulo__icontains=palabra))
        if estado is not None and estado!="Todos":
            queryset = queryset.filter(estado=estado)
        return queryset
