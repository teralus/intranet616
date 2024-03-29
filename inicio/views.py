from typing import Any
from django.shortcuts import render
from .models import Service, Incidence
from django.views.generic import ListView, DetailView


class ServicesListView(ListView):
    model = Service
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_update'] = Incidence.objects.last()
        return context    
    
    
    
class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incidence_data'] = Incidence.objects.filter(service_id = self.object.id)
        return context
    
class IncidencesListView(ListView):
    model = Incidence 
    


class IncidenceDetailView(DetailView):
    model = Incidence
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incidence_data'] = Incidence.objects.filter(service_id=self.object.service_id)
        return context