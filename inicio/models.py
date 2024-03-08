from django.db import models


class ServiceStatus(models.Model):
    description = models.CharField(max_length=50, verbose_name="Descripción")
    
    def __str__(self):
        return self.description
    

class Service(models.Model):
    name = models.CharField(max_length=50)
    status=models.ForeignKey("ServiceStatus", on_delete=models.PROTECT )
    
    def __str__(self):
        return self.name
    
    
class Incidence(models.Model):
    date = models.DateField(verbose_name="Fecha")
    resume = models.TextField(verbose_name="Resumen")
    service = models.ForeignKey("Service", on_delete=models.PROTECT)
    date_update = models.DateTimeField(auto_now= True, verbose_name="Última actualización")
    
    def __str__(self):
        return  self.resume
    
    
    


