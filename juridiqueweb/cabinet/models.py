from django.db import models
class ArticleBlog(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey('authentification.Utilisateur', on_delete=models.SET_NULL, null=True)


# Create your models here.
