# Gestion de l'administration

# Importation des librairies
from django.contrib import admin

from .models import Articles, ArticlesAdmin

# Enreistrement de l'administrateur
admin.site.register(Articles, ArticlesAdmin)