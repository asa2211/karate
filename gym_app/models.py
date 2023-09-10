from django.db import models
from murabbiylar.models import TrenerModel


class GymModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    coach = models.ForeignKey(TrenerModel, on_delete=models.CASCADE)
    email = models.EmailField()
    location = models.URLField(blank=True, null=True)
    open_time = models.DateField()
    gym_logo = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.name

