from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from calendary.models import Day, Month, Year


# Create your models here.
class Reservation(models.Model):
    day = models.ForeignKey(Day,null=True, on_delete=models.CASCADE)
    month = models.ForeignKey(Month,null=True ,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,null=True, on_delete=models.CASCADE)
    hour = models.TimeField( max_length=250)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.user.name} para {self.service_name} el {self.day} de {self.month}  a las {self.hour}"
