from django.urls import path
from dashboard.views import (
    
    dashboard_view,
    calendar_view,
)

app_name = 'dashboard'

urlpatterns = [
    
    path('',view=dashboard_view,name='dashboard'),
    path('calendar',view=calendar_view,name='calendar'),
    
]
