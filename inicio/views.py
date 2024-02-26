from django.shortcuts import render
from .models import Service, Incidence
from django.views.generic import ListView, DetailView


class ServicesListView(ListView):
    model = Service 
    template_name = "service.html"
    context_object_name = 'service'
    
class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"
    context_object_name = 'service'
 
class IncidenceDetailView(DetailView):
    model = Incidence
    template_name = "incidence_detail.html"
    context_object_name = 'incidence'
