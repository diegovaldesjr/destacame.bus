from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Horario, Reserva, Trayecto
from .serializer import TrayectoSerializer, HorarioSerializer, ReservaSerializer, ReservaReadSerializer

from django.db.models import Count
from datetime import date, datetime

# Create your views here.
class TrayectoList(APIView):

  def get(self, request, format=None):
    q1 = Trayecto.objects.all().values()

    for t in q1:
      cantidad_horarios = Horario.objects.filter(trayecto=t['id']).count()
      cantidad_reservas = Reserva.objects.filter(trayecto=t['id']).count()
      
      if(cantidad_horarios > 0):
        t['promedio_reservas'] = round((cantidad_reservas/cantidad_horarios), 2)
      else:
        t['promedio_reservas'] = 0

    trayecto = q1
    return Response(trayecto)
  
  def post(self, request, format=None):
    serializer = TrayectoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrayectoDetail(APIView):
  def get_object(self, pk):
    try:
      return Trayecto.objects.get(pk=pk)
    except Trayecto.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    trayecto = self.get_object(pk)
    serializer = TrayectoSerializer(trayecto)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    trayecto = self.get_object(pk)
    serializer = TrayectoSerializer(trayecto, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    trayecto = self.get_object(pk)
    trayecto.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class HorarioList(APIView):
  def get_object(self, pk):
    try:
      return Horario.objects.filter(trayecto=pk)
    except Horario.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):

    if len(request.query_params) > 0 and request.query_params["day"] and request.query_params["month"] and request.query_params["year"]:
      day = request.query_params["day"]
      month = request.query_params["month"]
      year = request.query_params["year"]

      if request.query_params["capacidad"]:
        capacidad= 10 - ((int(request.query_params["capacidad"]) * 10) / 100)
        horarios = Horario.objects.annotate(total_reservas = Count('reserva')).filter(trayecto=pk, fecha__year=year, fecha__month=month, fecha__day=day, total_reservas__lte=capacidad)
      else:
        horarios = Horario.objects.annotate(total_reservas = Count('reserva')).filter(trayecto=pk, fecha__year=year, fecha__month=month, fecha__day=day)
    else:
      horarios = self.get_object(pk)
    
    serializer = HorarioSerializer(horarios, many=True)
    return Response(serializer.data)
  
  def post(self, request, pk, format=None):
    serializer = HorarioSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HorarioDetail(APIView):
  def get_object(self, pk):
    try:
      return Horario.objects.get(pk=pk)
    except Horario.DoesNotExist:
      raise Http404

  def get(self, request, fk, pk, format=None):
    horario = self.get_object(pk)
    serializer = HorarioSerializer(horario)
    return Response(serializer.data)

  def put(self, request, fk, pk, format=None):
    horario = self.get_object(pk)
    serializer = HorarioSerializer(horario, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, fk, pk, format=None):
    horario = self.get_object(pk)
    horario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class HorarioReservaList(APIView):
  def get_object(self, pk):
    try:
      return Reserva.objects.filter(horario=pk)
    except Reserva.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    reservas = self.get_object(pk)
    serializer = ReservaReadSerializer(reservas, many=True)
    return Response(serializer.data)
  
  def post(self, request, pk, format=None):
    serializer = ReservaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasajeroReservaList(APIView):
  def get_object(self, pk):
    try:
      return Reserva.objects.filter(pasajero=pk)
    except Reserva.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    reservas = self.get_object(pk)
    serializer = ReservaReadSerializer(reservas, many=True)
    return Response(serializer.data)

class PasajeroReservaDetail(APIView):
  def get_object(self, pk):
    try:
      return Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
      raise Http404

  def get(self, request, fk, pk, format=None):
    horario = self.get_object(pk)
    serializer = HorarioSerializer(horario)
    return Response(serializer.data)

  def delete(self, request, fk, pk, format=None):
    reserva = self.get_object(pk)
    reserva.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)