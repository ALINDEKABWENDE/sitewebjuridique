from django import forms
from .models import ArticleBlog

class ArticleBlogForm(forms.ModelForm):
    class Meta:
        model = ArticleBlog
        fields = '__all__'
        widgets = {
            'date_publication': forms.DateInput(attrs={'type': 'date'}),
        }
