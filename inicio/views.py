from django.shortcuts import render
from .models import Service, Incidence
from django.views.generic import ListView, DetailView




class ServicesListView(ListView):
    model = Service 
    template_name = "service.html"
    
     
class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"
    
    
class IncidenceListView(ListView):
    model = Incidence
    template_name = "incidence.html"
    

class IncidenceDetailView(DetailView):
    model = Incidence
    template_name = "incidence_detail.html"
    
