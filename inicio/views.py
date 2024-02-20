from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service, Incidence
from django.views.generic import ListView, DetailView




class ServicesListView(ListView):
    model = Service 
    template_name = "index.html"
    
     
class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"
    
    
class IncidenceListView(ListView):
    model = Incidence
    template_name = "index.html"
    

class IncidenceDetailView(DetailView):
    model = Incidence
    template_name = "incidence_detail.html"
    
