from django.db import models

class CaseFan(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rpm = models.CharField(max_length=100)
    airflow = models.CharField(max_length=100)
    noise_level = models.CharField(max_length=100)