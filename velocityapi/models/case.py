from django.db import models

class Case(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    side_panel = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    cabinet_type = models.CharField(max_length=100)