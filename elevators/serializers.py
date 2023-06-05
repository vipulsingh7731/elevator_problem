from rest_framework import serializers

from .models import ElevatorSystem, Elevator, ElevatorRequest

class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = ('id', 'name', 'num_elevators', 'floors')
        
class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ('id', 'elevator_system', 'current_floor', 'direction', 'door_open', 'operational')