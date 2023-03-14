from django.db import models

class Keyboard(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    backlit = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    wireless = models.BooleanField(default=False)