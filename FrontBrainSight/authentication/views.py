from django.shortcuts import render
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AuthenticationView(LoginRequiredMixin,TemplateView):
    pass

auth_login_view = AuthenticationView.as_view(template_name=("authentication/auth-login.html"))
auth_register_view = AuthenticationView.as_view(template_name=("authentication/auth-register.html"))
auth_recover_password_view = AuthenticationView.as_view(template_name=("authentication/auth-recoverpw.html"))
auth_lock_screen_view = AuthenticationView.as_view(template_name=("authentication/auth-lock-screen.html"))