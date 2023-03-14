from django.db import models

class CpuCooler(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    is_water_cooled = models.BooleanField(default=False)
    rpm = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    noise_level = models.CharField(max_length=100)