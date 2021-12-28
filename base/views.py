from django.http import JsonResponse

from base.models import Scenery

from .timer import RepeatTimer

def test(msg):
    print(msg)

t = RepeatTimer(5, test, ['test'])
t.start()

def index(request):
    data = list(Scenery.objects.filter(stationHash='abcd').values())

    return JsonResponse(data, safe=False)
