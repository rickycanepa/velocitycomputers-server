from django.db import models

class GPU(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    storage_interface = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    clockSpeed = models.CharField(max_length=100)
    chipset = models.CharField(max_length=100)