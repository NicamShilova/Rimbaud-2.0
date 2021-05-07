# Importation des librairies
from django.contrib import admin
from django.urls import include, path

# Mise en place des liens des pages html
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]