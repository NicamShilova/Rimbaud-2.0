# Importation des librairies
from django.db import models
from django.contrib import admin

# Création de la classe Article
class Articles(models.Model):
    titre = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    article = models.CharField(max_length=256)
    date =  models.DateField()
    admin =  models.BooleanField()

# Création de la classe Article pour la partie administration
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('titre' , 'description' ,  'article' , 'date' ,  'admin')
    list_filter = ('titre',)

    def __str__(self):  
        return self.name
