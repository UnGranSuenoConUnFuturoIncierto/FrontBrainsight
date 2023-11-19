from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "inicio.html")

def informacion(request):
    return render(request, "informacion.html")