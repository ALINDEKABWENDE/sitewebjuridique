from django.shortcuts import render
from django.shortcuts import render
from .models import IndicateurMensuel

def tableau_mensuel(request, mois, année):
    stats = IndicateurMensuel.objects.filter(mois=mois, année=année).first()
    return render(request, 'statistiques/tableau_mensuel.html', {'stats': stats, 'mois': mois, 'année': année})

# Create your views here.
