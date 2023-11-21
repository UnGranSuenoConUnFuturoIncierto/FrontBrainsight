from django.urls import path
from authentication.views import (
    
    auth_login_view,
    auth_register_view,
    auth_recover_password_view,
    auth_lock_screen_view,
    
)

app_name = 'authentication'

urlpatterns = [
    
    path('login',view=auth_login_view,name='login'),
    path('register',view=auth_register_view,name='register'),
    path('recover_password',view=auth_recover_password_view,name='recover_password'),
    path('lock_screen',view=auth_lock_screen_view,name='lock_screen'),
    
    
    
]
