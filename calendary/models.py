from django.db import models


# Create your models here.
class Day(models.Model):
    day_of_month = models.IntegerField()

    def __str__(self):
        return f"Day {self.day_of_month}"


class Month(models.Model):
    month_name = models.CharField()

    def __str__(self):
        return f"Month {self.month_name}"


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return f"Year {self.year}"
