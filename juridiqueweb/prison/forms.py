from django import forms
from .models import Prisonnier, Activite, SuiviMedical

class PrisonnierForm(forms.ModelForm):
    class Meta:
        model = Prisonnier
        fields = '__all__'
        widgets = {
            'date_incarceration': forms.DateInput(attrs={'type': 'date'}),
            'date_liberation': forms.DateInput(attrs={'type': 'date'}),
        }

class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class SuiviMedicalForm(forms.ModelForm):
    class Meta:
        model = SuiviMedical
        fields = '__all__'
        widgets = {
            'date_visite': forms.DateInput(attrs={'type': 'date'}),
        }
