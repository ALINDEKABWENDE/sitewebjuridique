from django.shortcuts import render
from django.shortcuts import render
from .models import Client

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste_clients.html', {'clients': clients})


# Create your views here.
