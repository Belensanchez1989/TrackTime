from django.db import models


# Create your models here.

class Service(models.Model):
    services = models.CharField( null=True,max_length=80)

    def __str__(self):
        return f"Servicio: {self.service_name} seleccionado"
