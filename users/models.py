from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(null=True,max_length=80)
    last_name = models.CharField(null=True,max_length=80)
    email = models.EmailField(null=True,max_length=100)
    service = models.CharField(max_length=100, null=True)

    def __srt__(self):
        return f"Persona: {self.name} {self.last_name}"
