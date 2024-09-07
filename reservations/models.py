from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):
    date = models.DateField(max_length=250)
    hour = models.TimeField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.user} el {self.date} a las {self.hour}"
