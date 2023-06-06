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
