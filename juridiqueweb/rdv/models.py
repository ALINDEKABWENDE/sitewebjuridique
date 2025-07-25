from django.db import models
class RendezVous(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    date = models.DateTimeField()
    sujet = models.CharField(max_length=150)
    statut = models.CharField(max_length=20, choices=[
        ('à_venir', 'À venir'),
        ('terminé', 'Terminé'),
        ('annulé', 'Annulé'),
    ])


# Create your models here.
