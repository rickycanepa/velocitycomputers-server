from django.db import models

class Mouse(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tracking_method = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    wireless = models.BooleanField(default=False)