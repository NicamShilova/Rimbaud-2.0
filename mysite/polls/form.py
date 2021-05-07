# Importation des librairies
from django.forms import ModelForm
from polls.models import Articles

# Ajout des attributs dans la base de données
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['titre' , 'description' , 'article' , 'date' , 'admin']