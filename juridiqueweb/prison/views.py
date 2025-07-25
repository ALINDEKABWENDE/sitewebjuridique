from django.shortcuts import redirect, render
from django.shortcuts import render

#from juridiqueweb.prison.forms import PrisonnierForm
from .models import Prisonnier
#from juridiqueweb.prison.forms import PrisonnierForm
from .forms import PrisonnierForm


def liste_prisonniers(request):
    prisonniers = Prisonnier.objects.all()
    return render(request, 'prison/liste_prisonniers.html', {'prisonniers': prisonniers})
def ajouter_prisonnier(request):
    if request.method == 'POST':
        form = PrisonnierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_prisonniers')  # ou autre vue
    else:
        form = PrisonnierForm()
    return render(request, 'prison/ajouter_prisonnier.html', {'form': form})
# Create your views here.
