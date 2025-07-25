from django.db import models
class IndicateurMensuel(models.Model):
    mois = models.CharField(max_length=2, choices=[
        ("01", "Janvier"), ("02", "Février"), ("03", "Mars"),
        ("04", "Avril"), ("05", "Mai"), ("06", "Juin"),
        ("07", "Juillet"), ("08", "Août"), ("09", "Septembre"),
        ("10", "Octobre"), ("11", "Novembre"), ("12", "Décembre"),
    ])
    année = models.PositiveIntegerField()
    nombre_dossiers_ouverts = models.PositiveIntegerField()
    nombre_prisonniers_admis = models.PositiveIntegerField()
    nombre_rendez_vous = models.PositiveIntegerField()


# Create your models here.
