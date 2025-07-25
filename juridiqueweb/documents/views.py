from django.shortcuts import render
from django.shortcuts import render
from .models import Document

def liste_documents(request):
    documents = Document.objects.all()
    return render(request, 'documents/liste_documents.html', {'documents': documents})


# Create your views here.
