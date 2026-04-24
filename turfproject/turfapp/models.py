from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()