# Importation des librairies
from django.urls import path

from . import views

# Mise en place des liens des pages html
urlpatterns = [
    path('', views.index, name='index'),
    path('information/', views.information, name='information'),
]