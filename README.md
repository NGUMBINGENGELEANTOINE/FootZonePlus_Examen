Ce projet consiste à développer une application web de vente de billets pour un match de football avec intégration d'une réservation automatique des places au sein du stade.

Outils utilisés :
=================

1. Python : Pourquoi python ? parce que il est facile à prendre en main par rapport à d'autres langages de programmation, il est utilisé dans presque tous les domaines et il a un syntaxe très facile à comprendre.

2. Django : Framework de Python basé sur le modèle MVC (Modèle Vue Controlleur): Utilisé pour le Backend, permet d'intéragir avec la BD, de faire le CRUD et développer toute la structure backend de l'application. La puissance de Django est qu' il vient avec une BD déjà intégrée dans le projet, La sécurité est déjà mise en place, donc django s'occupe de la sécurité de notre application, de sessions, la gestion des utilisateurs, les groupes déjà disponibles, Une interface d'administration complète est en place et le chiffrage des mots de passe automatique est déjà en place. Ce qui est bien aussi avec Django, il vient avec un serveur local intégré qui nous permet de lancer directement nos applis sans installer un autre serveur.

3. Html 5: Pour concevoir la structure des pages web.

4. CSS 3: Pour styliser nos pages web.

5. Bootstrap : Framework css utilisé pour la mise en forme et le style dans une application web.

6. SQLite : BD intégrée dans le projet django directement pour stocker les données

7. Git et Github : Pour le versionnage du projet.


========================================================================================


Comment Exécuter le Projet ?
============================

Voici les étapes à suivre :

1. Ouvrer l'invite commande cmd à la racine du projet
2. Activer l'environnement virtuel du projet avec la commande :

    env\Scripts\activate

3. Installer les dépendances nécessaires pour le projet en exécutant la commande suivante :

    pip install -r requirements.txt

4. Lancer le serveur :

    python manage.py runserver

5. Copier l'adresse ip locale du serveur et coller ça dans un navigateur Web. ou bien vous faite : ctrl + clic gauche du clavier sur le lien, il s'ouvrira automatiquement.

    Vous allez arriver à la page d'accueil du site.

    Pour accéder à la Partie admin du projet, après l'url taper : /admin
    la page connexion s'ouvrira puis connectez - vous en tant que administrateur avec les identifiants :
    - Nom d'utilisateur : admin
    - Mot de passe : admin

======================================================================================

Structure du projet :
=====================

Dans un projet django nous pouvons avoir plusieurs applications utilisées dans un seul projet et chaque application avec son role et ses fonctionalités. Le projet django est structuré de cette manière :

1. le fichier : manage.py

Ce fichier nous permet de lancer notre serveur ou exécuter le projet, créer un super utilisateur (super administrateur), lancer et voir les migrations de la BD, ...

! : Pour quitter le serveur on utilise le raccourcis clavier : ctrl + c.

2. le fichier : settings.py

Ce fichier nous permet de configurer notre projet et nos applications.

3. les fichiers du projet et de l'application : urls.py

Ces fichiers sont les memes urls.py de l'appli et du projet, ils jouent le role de redirection ou le chemin d'accès reliant les pages.

4. le fichier : admin.py

Permet de gérer l'interface admin par défaut de django

5. le fichier : models.py

Ce fichier contient les classes de la BD (toutes les tables de notre application sont créées ici ). Les classes représentent les tables dans django. et toutes les relations se font ici. Les clés primaires sont gérer par défaut avec django.

6. le fichier : views.py

Ce fichier gère les fonctions pour retourner une vue, et gère également toutes les opérations CRUD de l'application.

7. le fichier : tests.py

Permet de faire les tests unitaires

8. le fichier : wsgi.py

Gère la mise en production de l'application sur un serveur en ligne (l'hebergement).

9. les fichiers __inti__.py

Gère toutes les migrations effectuées dans le projet.

10. le fichier forms.py 

Permet de créer les formulaires sans passer par les fichiers html. ici on crée les formulaires en héritant de la classe UserCreationForm de django puis on appel le formulaire dans le fichier html.

11. le dossier : templates

Ce dossier contient tous nos fichiers html pour la structure de notre projet. C'est la norme avec django de créer un dossier templates. et ce dossier est sensible à la casse.

12. le dossier des Migrations:

Toutes nos listes de migrations vers la BD sont listées ici. 

13. le dossier static:

Ce dossier gère le fichier css pour le style et on peut y mettre les images aussi



