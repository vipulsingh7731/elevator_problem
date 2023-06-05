from django.db import models

# Create your models here.
class ElevatorSystem(models.Model):
    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=200)
    floors = models.IntegerField(default=0)
    num_elevators = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} - {self.num_elevators} elevators"
                                      
class Elevator(models.Model):
    id = models.AutoField(primary_key=True)
    elevator_system = models.ForeignKey(ElevatorSystem, on_delete=models.CASCADE)
    current_floor = models.IntegerField(default=0)
    DIRECTION_CHOICES = (
    ("1", "1"), #Up
    ("0", "0"), #Stationary
    ("-1", "-1"), #Down
    )
    direction = models.CharField(max_length=2, choices=DIRECTION_CHOICES, default="0")
    door_open = models.BooleanField(default=False)
    operational = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Elevator: " + str(self.id) + " Elevator System: " + str(self.elevator_system)

class ElevatorRequest(models.Model):
    id = models.AutoField(primary_key=True)
    elevator_system = models.ForeignKey(ElevatorSystem, on_delete=models.CASCADE)
    called_at = models.IntegerField(default=0)
    destination_floor = models.IntegerField(default=0)
    DIRECTION_CHOICES = (
    ("1", "1"), #Up
    ("0", "0"), #Stationary
    ("-1", "-1"), #Down
    )
    direction = models.CharField(max_length=2, choices=DIRECTION_CHOICES, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Elevator System: " + str(self.elevator_system) + " Called At: " + str(self.called_at) 

