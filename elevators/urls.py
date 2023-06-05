from django.urls import path
from . import views

app_name = 'elevators'
urlpatterns = [
    path('init/', views.ElevatorInitView.as_view(), name='elevator_list'),
    path('', views.ElevatorSystemListView.as_view(), name='elevator_system_list'),
    path('<int:pk>/', views.ElevatorSystemDetailView.as_view(), name='elevator_system_detail'),
    path('<int:pk>/elevator/<int:elev_id>/', views.ElevatorSystemDetailUpdateView.as_view(), name='detail_update_elevator'),
    # path('request/', views.ElevatorRequestView.as_view(), name='elevator_request'),
]