from django.db import models
class Prisonnier(models.Model):
    nom = models.CharField(max_length=100)
    numero_dossier = models.CharField(max_length=50, unique=True)
    date_incarceration = models.DateField()
    date_liberation = models.DateField(null=True, blank=True)
    infraction = models.TextField()
    centre_detention = models.CharField(max_length=100)
    statut_medical = models.TextField(blank=True)

class Activite(models.Model):
    prisonnier = models.ForeignKey(Prisonnier, on_delete=models.CASCADE)
    type_activite = models.CharField(max_length=100)
    date = models.DateField()
    remarque = models.TextField(blank=True)

class SuiviMedical(models.Model):
    prisonnier = models.ForeignKey(Prisonnier, on_delete=models.CASCADE)
    date_visite = models.DateField()
    diagnostic = models.TextField()
    traitement = models.TextField()


# Create your models here.
