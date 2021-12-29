from .models import Pasajero, Terminal, Chofer, Bus, Asiento, Trayecto, Horario, Reserva, UserProfile
from rest_framework import serializers

class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = '__all__'

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = '__all__'

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

    def create(self, validated_data):
        bus = Bus.objects.create(**validated_data)
        
        i=1
        for i in range(1,11):
            Asiento.objects.create(n_asiento=i, bus=bus)

        return bus

class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class ReservaReadSerializer(serializers.ModelSerializer):
    horario = HorarioSerializer(read_only=True)
    pasajero = PasajeroSerializer(read_only=True)
    asiento = AsientoSerializer(read_only=True)
    trayecto = TrayectoSerializer(read_only=True)
    class Meta:
        model = Reserva
        fields = '__all__'