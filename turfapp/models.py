from django.db import models
from django.contrib.auth.models import User
class Slot(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.time}"


class Booking(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.slot}"
