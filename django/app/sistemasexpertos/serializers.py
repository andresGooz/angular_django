from rest_framework import serializers
from .models import Ticket
from django.utils import timezone
import datetime



class TicketSerializer(serializers.ModelSerializer):
    creado_hace = serializers.SerializerMethodField('tiempo_diferencia')
    def tiempo_diferencia(self, obj):
      try:
          segundos = (timezone.localtime() - obj.datetime).seconds
          return str(datetime.timedelta(seconds=segundos))
      except:
          return 0
    class Meta:
        model = Ticket
        fields = '__all__'
        extra_fields = ['creado_hace']
