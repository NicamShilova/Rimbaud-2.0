# Rimbaud 2.0




### Un écrivain veut se mettre au numérique et vous demande de lui réaliser une application web pour publier ses articles sur les internets !


## Pré-requis

```
Python
Anaconda
django
```


## Installation

Installer Anaconda

Installer vscode

Dans Anaconda, créer un environnement, puis installer dedans django :

```
python -m pip install Django
```


## Exécution

Dans vscode, charger d'abord l'environnement puis lancer vscode

Ouvrir un shell, puis aller dans le dossier mysite :

```
cd mysite
```

Initialiser la base de données :

```
python manage.py makemigrations mysite
python manage.py migrate
```

Ajouter des données la base:

```
- Dans un navigateur, aller à l'adresse : http://127.0.0.1:8000/admin/polls/articles/
- Créer le polls Articles, puis le sélectionner
- Cliquer sur Add Article
- Remplir le formulaire, et valider
- Répéter autant de fois que nécessaire
```

Note : la case admin permet d'afficher l'article dans le navigateur


Lancer le serveur :

```
python manage.py runserver
```


Lancer le site internet : 

```
http://127.0.0.1:8000/polls/
```