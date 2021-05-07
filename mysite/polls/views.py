# Importation des classes et des librairies
from django.shortcuts import render , redirect
from .form import ArticlesForm
from polls.models import Articles

from datetime import date

# Gestion de la liste des articles
def index(request):
    donnes_article = {'dataObject': Articles.objects.all().filter(admin=1)}
    return render(request , 'index.html' , donnes_article)

# Gestion de l'affichage des informations sur les articles
def information(request):
    recherche = int(request.GET.get('id', ''))
    donnes_article = {'dataObject': Articles.objects.all().filter(id=recherche, admin=1), 'recherche' : recherche}

    return render(request , 'information.html' , donnes_article)