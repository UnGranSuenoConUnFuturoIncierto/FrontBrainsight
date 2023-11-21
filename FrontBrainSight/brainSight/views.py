from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import BadHeaderError, message, send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

# Index Pages
def index(request):
    return render(request,"index/index.html")

class MyPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    success_url = reverse_lazy("dashboard:dashboard")


class MyPasswordSetView(LoginRequiredMixin,PasswordSetView):
    success_url = reverse_lazy("dashboard:dashboard")