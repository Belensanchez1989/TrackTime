from django.db import models


# Create your models here.
class Hour(models.Model):
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['start_hour', 'end_hour'], name='unique_hour')
        ]

    def __str__(self):
        return f"{self.start_hour} - {self.end_hour}"