from django.db import models
class Client(models.Model):
    nom_complet = models.CharField(max_length=150)
    email = models.EmailField()
    téléphone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)
    date_inscription = models.DateField(auto_now_add=True)

class DossierJuridique(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    statut = models.CharField(max_length=50, choices=[
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('clos', 'Clos')
    ])
    date_ouverture = models.DateField()
    date_clôture = models.DateField(null=True, blank=True)

# Create your models here.
