from django.shortcuts import render
from django.shortcuts import render
from .models import ArticleBlog

def accueil(request):
    articles = ArticleBlog.objects.order_by('-date_publication')[:5]
    return render(request, 'cabinet/accueil.html', {'articles': articles})

# Create your views here.
