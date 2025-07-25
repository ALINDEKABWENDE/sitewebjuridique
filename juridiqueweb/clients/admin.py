#from django.contrib import admin
from django.contrib import admin
from .models import Client, DossierJuridique

admin.site.register(Client)
admin.site.register(DossierJuridique)

# Register your models here.
