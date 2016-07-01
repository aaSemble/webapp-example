from django.db import models

class Request(models.Model):
    source_ip = models.GenericIPAddressField()
    handler = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
