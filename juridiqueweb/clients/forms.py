from django import forms
from .models import Client, DossierJuridique

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class DossierJuridiqueForm(forms.ModelForm):
    class Meta:
        model = DossierJuridique
        fields = '__all__'
        widgets = {
            'date_ouverture': forms.DateInput(attrs={'type': 'date'}),
            'date_clôture': forms.DateInput(attrs={'type': 'date'}),
        }
