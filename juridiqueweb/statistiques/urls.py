from django.urls import path
from . import views

urlpatterns = [
    path('<str:mois>/<int:année>/', views.tableau_mensuel, name='tableau_mensuel'),
]
