from django.urls import path
from pages.views import (
    
    pages_starter,
    pages_maintenance,
    pages_coming_soon,
    pages_timeline,
    pages_gallery,
    pages_faqs,
    pages_pricing,
    pages_error404,
    pages_error500,
    
)

app_name = 'pages'

urlpatterns = [
    
    path('starter',view=pages_starter,name='starter'),
    path('maintenance',view=pages_maintenance,name='maintenance'),
    path('coming_soon',view=pages_coming_soon,name='coming_soon'),
    path('timeline',view=pages_timeline,name='timeline'),
    path('gallery',view=pages_gallery,name='gallery'),
    path('faqs',view=pages_faqs,name='faqs'),
    path('pricing',view=pages_pricing,name='pricing'),
    path('error404',view=pages_error404,name='error404'),
    path('error500',view=pages_error500,name='error500'),
    
]
