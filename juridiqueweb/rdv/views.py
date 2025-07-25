from django.shortcuts import render
from django.shortcuts import render
from .models import RendezVous

def liste_rdv(request):
    rdvs = RendezVous.objects.select_related('client').all()
    return render(request, 'rdv/liste_rdv.html', {'rdvs': rdvs})

# Create your views here.
