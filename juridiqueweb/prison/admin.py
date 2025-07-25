from django.contrib import admin
from .models import Prisonnier, Activite, SuiviMedical

admin.site.register(Prisonnier)
admin.site.register(Activite)
admin.site.register(SuiviMedical)


# Register your models here.
