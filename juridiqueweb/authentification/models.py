from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('juriste', 'Juriste'),
        ('assistant', 'Assistant'),
        ('agent_penitentiaire', 'Agent pénitentiaire'),
        ('client', 'Client'),
    ]
    rôle = models.CharField(max_length=30, choices=ROLE_CHOICES)


# Create your models here.
