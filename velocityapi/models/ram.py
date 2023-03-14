from django.db import models

class RAM(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    type = models.CharField(max_length=100)