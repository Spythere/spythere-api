from django.db import models

# Scenery model - nieużywane
# class Scenery(models.Model):
#     stationHash = models.CharField(max_length=100, unique=True)
#     stationName = models.CharField(max_length=100)

#     currentDispatcherName = models.CharField(max_length=100, null=True)
#     currentDispatcherId = models.IntegerField(null=True)
#     currentDispatcherFrom = models.DateTimeField(auto_now=True)
    
#     dispatcherHistory = models.JSONField(default=dict) 

# Station model - do przechowywania danych o scenerii
class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    project_lines = models.CharField(max_length=200, null=True)
    project_name = models.CharField(max_length=100, null=True)
    req_level = models.IntegerField(null=True)
    supporters_only = models.BooleanField(default=False)
    signal_type = models.CharField(max_length=50)
    control_type = models.CharField(max_length=50)
    sbl_routes = models.CharField(max_length=200, null=True)
    twb_routes = models.CharField(max_length=200, null=True)
    track_oneway_e = models.IntegerField()
    track_oneway_ne = models.IntegerField()
    track_twoway_e = models.IntegerField()
    track_twoway_ne = models.IntegerField()
    checkpoints = models.CharField(max_length=200, null=True)

    is_default = models.BooleanField(default=False)
    is_nonpublic = models.BooleanField(default=False)
    is_unavailable = models.BooleanField(default=False)