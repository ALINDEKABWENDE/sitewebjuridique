from django.db import models
class Document(models.Model):
    titre = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='documents/')
    date_upload = models.DateTimeField(auto_now_add=True)
    lié_au_dossier = models.ForeignKey('clients.DossierJuridique', on_delete=models.CASCADE, null=True, blank=True)
    visible_par_client = models.BooleanField(default=True)

# Create your models here.
