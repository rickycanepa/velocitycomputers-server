from django.db import models

class SSD(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    m2 = models.BooleanField(default=False)