from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PagesView(LoginRequiredMixin,TemplateView):
    pass

pages_starter = PagesView.as_view(template_name="pages/pages-starter.html")
pages_maintenance = PagesView.as_view(template_name="pages/pages-maintenance.html")
pages_coming_soon = PagesView.as_view(template_name="pages/pages-comingsoon.html")
pages_timeline = PagesView.as_view(template_name="pages/pages-timeline.html")
pages_gallery = PagesView.as_view(template_name="pages/pages-gallery.html")
pages_faqs = PagesView.as_view(template_name="pages/pages-faqs.html")
pages_pricing = PagesView.as_view(template_name="pages/pages-pricing.html")
pages_error404 = PagesView.as_view(template_name="pages/pages-404.html")
pages_error500 = PagesView.as_view(template_name="pages/pages-500.html")