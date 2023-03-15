from django.db import models

class HelpRequest(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='computer')
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=500) 