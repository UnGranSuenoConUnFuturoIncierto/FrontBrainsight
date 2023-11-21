from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class E_mailView(LoginRequiredMixin,TemplateView):
    pass

email_inbox = E_mailView.as_view(template_name = "e_mail/email-inbox.html")
email_read = E_mailView.as_view(template_name = "e_mail/email-read.html")
email_compose = E_mailView.as_view(template_name = "e_mail/email-compose.html")