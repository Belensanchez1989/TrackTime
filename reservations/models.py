from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Reservation(models.Model):
    date = models.DateField(null=True)
    end_hour = models.TimeField(null=True,max_length=250)
    start_hour = models.TimeField(null=True,max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"Reserva de {self.user.name}  el{self.date} a las {self.start_hour} hasta las {self.end_hour} "
