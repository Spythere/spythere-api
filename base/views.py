from django.http import JsonResponse

from base.models import Scenery

def index(request):
    data = list(Scenery.objects.filter(stationHash='abcd').values())

    return JsonResponse(data, safe=False)
