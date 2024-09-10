from django.db import models


# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=80)

    def __str__(self):
        return f"Servicio: {self.service_name} seleccionado"
