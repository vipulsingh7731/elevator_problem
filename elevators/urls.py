from django.urls import path
from . import views

app_name = 'elevators'
urlpatterns = [
    path('init/', views.ElevatorInitView.as_view(), name='elevator_list'),
    path('', views.ElevatorSystemListView.as_view(), name='elevator_system_list'),
    path('<int:pk>/', views.ElevatorSystemDetailView.as_view(), name='elevator_system_detail'),
    
    path('<int:elev_system>/elevator/<int:id>/', views.ElevatorSystemDetailUpdateView.as_view(), name='detail_update_elevator'),
    path('<int:elev_system>/elevator/<int:id>/requests/', views.SpecElevatorRequestView.as_view(), name='detail_elevator_requests'),
    path('<int:elev_system>/elevator/<int:id>/direction/', views.ElevatorDirectionView.as_view(), name='elevator_direction'),
    path('<int:elev_system>/elevator/<int:pk>/operational/', views.ElevatorOperationalView.as_view(), name='elevator_operational'),
    path('<int:elev_system>/elevator/<int:pk>/door/', views.ElevatorDoorView.as_view(), name='elevator_door'),
    
    #All requests 
    path('request/', views.ElevatorRequestView.as_view(), name='elevator_request'),
]