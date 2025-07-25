from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_prisonniers, name='liste_prisonniers'),
    path('ajouter/', views.ajouter_prisonnier, name='ajouter_prisonnier'),
]
