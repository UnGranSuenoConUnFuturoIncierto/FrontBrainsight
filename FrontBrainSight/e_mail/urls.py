from django.urls import path
from e_mail.views import (
    
    email_inbox,
    email_read,
    email_compose,
    
)

app_name="e_mail"

urlpatterns = [
    
    path('inbox',view=email_inbox,name='inbox'),
    path('read',view=email_read,name='read'),
    path('compose',view=email_compose,name='compose'),
    
]
