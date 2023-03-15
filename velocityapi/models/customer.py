from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)