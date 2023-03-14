from django.db import models

class HelpRequest(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='computer')
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=500) 