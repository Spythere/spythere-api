from django.http import JsonResponse

from base.models import Scenery
import json
# import requests

# Create your views here.

def index(request):
    data = list(Scenery.objects.filter(stationHash='abcd').values())

    return JsonResponse(data, safe=False)
