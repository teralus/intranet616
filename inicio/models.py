from django.db import models


class ServiceStatus(models.Model):
    description = models.TextField(verbose_name="Descripción")
    
    def __str__(self):
        return self.description
    

class Service(models.Model):
    description = models.TextField(verbose_name="Descripción")
    status=models.ForeignKey("ServiceStatus", on_delete=models.PROTECT )
    
    def __str__(self):
        return {self.description}, {self.status}
    
    
class Incidence(models.Model):
    date = models.DateField(verbose_name="Fecha")
    resume = models.TextField(verbose_name="Resumen")
    service = models.ForeignKey("Service", on_delete=models.PROTECT)
    
    def __str__(self):
        return {self.date}, {self.resume}, {self.duration}
    
    
    


