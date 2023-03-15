from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE, related_name='favorite')