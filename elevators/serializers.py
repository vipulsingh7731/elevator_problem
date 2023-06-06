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

class ElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = ('id', 'elevator_system', 'elevator', 'called_at', 'destination_floor', 'direction')
        
        
class SpecElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = ('id', 'called_at', 'destination_floor', 'direction', 'status')
        
        
class ElevatorOperationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ('operational',)

class ElevatorDoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ('door_open',)