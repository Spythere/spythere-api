from django.db import models

# Create your models here.
class Scenery(models.Model):
    stationHash = models.CharField(max_length=100, unique=True)
    stationName = models.CharField(max_length=100)

    currentDispatcherName = models.CharField(max_length=100, null=True)
    currentDispatcherId = models.IntegerField(null=True)
    currentDispatcherFrom = models.DateTimeField(auto_now=True)
    
    dispatcherHistory = models.JSONField(default=dict) 