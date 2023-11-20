from django.urls import path
from . import views

urlpatterns = [
    path("select/", views.home, name="home"),
    path("resultado/", views.informacion, name="resultado")
]