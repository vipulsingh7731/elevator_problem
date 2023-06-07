# Elevator Problem

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Thought Process
I have tried to make the API and model w.r.t. an external Elevator System, since the Elevator System can be quite complex with multiple elevators. 
The models present are **ElevatorSystem** (so the system can have multiple elevator systems), **Elevator** (Each elevator is assoiciated with an Elevator system and has all the required functionalities told in problem statement), **ElevatorRequest** (which are all the requests generated, fulfilled or not regardless. Each is associated with an **Elevator** and an **ElevatorSystem**).

## Architecture
    
 ### Urls.py
 *[POST Only]* - Initialise the elevator system from this Endpoint
    
    $ path('elevator_system/init/', views.ElevatorInitView.as_view(), name='elevator_list'),
 *[GET Only]* - Gets all the elevator's current state for an elevator system
            
    $ path('elevator_system/<int:pk>/', views.ElevatorSystemDetailView.as_view(), name='elevator_system_detail'), 
 *[GET, POST]* - Detailed View of an elevator
  
    $ path('elevator_system/<int:elev_system>/elevator/<int:id>/', ...as_view(), name='detail_update_elevator'),
 *[GET, POST]* - Fetches all the requests "unfulfilled" for a given elevator, and all requests for a particular elevator should POST here
    
    $ path('elevator_system/<int:elev_system>/elevator/<int:id>/requests/', ...as_view(), name='detail_elevator_requests'), 
 *[GET Only]*  - Fetch the current direction for a given elevator
   
    $ path('elevator_system/<int:elev_system>/elevator/<int:id>/direction/', ...as_view(), name='elevator_direction'), 
 *[GET, POST]* - Get operational status from here and Update it too from here
    
    $ path('elevator_system/<int:elev_system>/elevator/<int:pk>/operational/', ...as_view(), name='elevator_operational'), 
 *[POST Only]* - Update Door status from here

    $ path('elevator_system/<int:elev_system>/elevator/<int:pk>/door/', ...as_view(), name='elevator_door'), 
### Models
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
        elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
        called_at = models.IntegerField(default=0)
        DIRECTION_CHOICES = (
        ("1", "1"), #Up
        ("0", "0"), #Stationary
        ("-1", "-1"), #Down
        )
        status = models.BooleanField( default=0) #0 = pending, 1 = completed
        destination_floor = models.IntegerField(default=0)
        direction = models.CharField(max_length=2, choices=DIRECTION_CHOICES, default="1")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return "Elevator System: " + str(self.elevator_system) + " Called At: " + str(self.called_at) 
## Setup
Docker is required for this to run.
    For Local development, run
    
    $ docker-compose -f local.yml build
Below command needs to be run whenever the service is used, "build" is not required to be run every time.
    
    $ docker-compose -f local.yml up
For production, use
    
    $ docker-compose -f production.yml build
    $ docker-compose -f production.yml up
## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
