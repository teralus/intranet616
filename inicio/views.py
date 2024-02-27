from typing import Any
from django.shortcuts import render
from .models import Service, Incidence
from django.views.generic import ListView, DetailView


class ServicesListView(ListView):
    model = Service 
    template_name ='services.html'
    context_object_name = 'services'
    
class ServiceDetailView(DetailView):
    model = Service
    template_name= 'service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incidence_data'] = Incidence.objects.filter(service_id = self.object.id)
        return context
         
    
class IncidencesListView(ListView):
    model = Incidence 
    
 
class IncidenceDetailView(DetailView):
    model = Incidence
    template_name = 'incidence_detail.html'
    context_object_name = 'incidence'

