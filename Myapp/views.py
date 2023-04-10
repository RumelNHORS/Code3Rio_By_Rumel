from django.shortcuts import render
from django.views import generic    #Add By Rumel
from django.views.generic import TemplateView   #Add By Rumel

# Create your views here.

class HomeView(TemplateView):
    template_name = "Myapp/index.html"
