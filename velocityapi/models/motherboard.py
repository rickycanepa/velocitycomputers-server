from django.db import models

class Motherboard(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.DecimalField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    form_factor = models.CharField(max_length=100)
    chipset = models.CharField(max_length=100)
    memory_slots = models.CharField(max_length=100)
    socket_type = models.CharField(max_length=100)