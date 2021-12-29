from rest_framework import viewsets

from .models import Pasajero, Terminal, Chofer, Bus, Asiento, Reserva, UserProfile
from .serializer import AsientoSerializer, BusSerializer, ChoferSerializer, PasajeroSerializer, ReservaReadSerializer, TerminalSerializer, UserSerializer

class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

class ChoferViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer

class ReservaReadViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaReadSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer