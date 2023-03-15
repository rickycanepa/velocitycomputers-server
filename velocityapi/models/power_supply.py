from django.db import models

class PowerSupply(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.DecimalField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    efficiency = models.CharField(max_length=100)