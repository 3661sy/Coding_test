from django.db import models
from django.utils import timezone

class car(models.Model):
    user = models.CharField(max_length=30)
    accident = models.BooleanField()
    repair = models.TextField()
    manufacturer = models.CharField(max_length=10)
    price = models.IntegerField()
    
    def __str__(self):
        return self.manufacturer

class draft(models.Model):
    user = models.CharField(max_length=30)
    accident = models.BooleanField(null=True, blank=True)
    repair = models.TextField(null=True, blank=True)
    manufacturer = models.CharField(max_length=10, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.manufacturer

class CarPhoto(models.Model):
    car_post = models.ForeignKey(car, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)