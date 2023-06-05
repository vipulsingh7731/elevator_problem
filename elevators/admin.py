from django.contrib import admin

# Register your models here.
from .models import ElevatorSystem, Elevator, ElevatorRequest
admin.site.register(ElevatorSystem)
admin.site.register(Elevator)
admin.site.register(ElevatorRequest)