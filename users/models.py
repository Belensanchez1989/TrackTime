from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __srt__(self):
        return f"Persona: {self.name} {self.last_name}"
