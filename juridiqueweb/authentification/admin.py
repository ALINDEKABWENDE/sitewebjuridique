from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

admin.site.register(Utilisateur, UserAdmin)


# Register your models here.
