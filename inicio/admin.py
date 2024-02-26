from django.contrib import admin
from .models import Service, Incidence, ServiceStatus


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    
@admin.register(Incidence)
class IncidenceAdmin(admin.ModelAdmin):
    list_display =('service', 'resume', 'date')
    
@admin.register(ServiceStatus)
class ServiceStatusAdmin(admin.ModelAdmin):
    list_display = ('description', )
    
    
    

