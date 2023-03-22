from django.db import models
from django.contrib.auth.models import User
from .customer import Customer
from .computer import Computer

class Favorite(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='customer_favorites')
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE, related_name='computer_favorites')