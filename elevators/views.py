from django.shortcuts import render

from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, HttpResponse

from .models import ElevatorSystem, Elevator, ElevatorRequest
from .serializers import ElevatorSystemSerializer, ElevatorSerializer
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

    
class ElevatorSystemDetailUpdateView(generics.ListCreateAPIView):
    
    lookup_field = 'elevator_system'
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
     
    # ElevatorSystemDetailUpdateView