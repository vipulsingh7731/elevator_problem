from django.shortcuts import render

from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, HttpResponse

from .models import ElevatorSystem, Elevator, ElevatorRequest
from .serializers import (ElevatorSystemSerializer, ElevatorSerializer, 
                    ElevatorRequestSerializer , SpecElevatorRequestSerializer, ElevatorOperationalSerializer,
                    ElevatorDoorSerializer
                    )
# Create your views here.

class ElevatorInitView(generics.CreateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            for i in range(int(serializer.data['num_elevators'])):
                Elevator.objects.create(elevator_system=get_object_or_404(ElevatorSystem, pk=serializer.data['id']))
            return Response(serializer.data)
        return Response(serializer.errors)

class ElevatorSystemListView(generics.ListAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
    
class ElevatorSystemDetailView(generics.ListAPIView):
    # lookup_field = 'pk'
    
    queryset = Elevator.objects.all()
    def get_queryset(self):
        return Elevator.objects.filter(elevator_system=get_object_or_404(ElevatorSystem, pk=self.kwargs['pk']))
    
    serializer_class = ElevatorSerializer

    
class ElevatorSystemDetailUpdateView(generics.RetrieveUpdateAPIView):
    
    lookup_field = 'id'
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    
    
# View to Fetch all requests for a given elevator
class SpecElevatorRequestView(generics.ListCreateAPIView):
    queryset = ElevatorRequest.objects.all()
    serializer_class = SpecElevatorRequestSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = SpecElevatorRequestSerializer(data=request.data)
        
        
        if serializer.is_valid():
            serializer.save(
                elevator=get_object_or_404(Elevator, pk=self.kwargs['id']), 
                elevator_system = get_object_or_404(ElevatorSystem, pk=self.kwargs['elev_system'])
            )
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def get_queryset(self):
        return ElevatorRequest.objects.filter(elevator=get_object_or_404(Elevator, pk=self.kwargs['id']), status=0)
     

     
# View to get current direction of a given elevator
class ElevatorDirectionView(generics.GenericAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    
    def get(self, request, *args, **kwargs):
        elevator = get_object_or_404(Elevator, pk=self.kwargs['id'])
        
        return Response(elevator.direction)
    
     
class ElevatorRequestView(generics.ListAPIView):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer
    
class ElevatorOperationalView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorOperationalSerializer
    
    def get(self, request, *args, **kwargs):
        elevator = get_object_or_404(Elevator, pk=self.kwargs['pk'])
        
        return Response(elevator.operational)
    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class ElevatorDoorView(generics.UpdateAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorDoorSerializer
    
    
    
    