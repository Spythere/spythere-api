from django.shortcuts import render

# Create your views here.

def managerView(request):
    return render(request, 'station_mgr/login_page.html', {'test': 123})
