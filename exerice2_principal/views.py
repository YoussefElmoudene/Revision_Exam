from datetime import timedelta
from time import timezone

from django.shortcuts import render

from exerice2_principal.models import Livre, Etudiant, Emprunteur


#  a) Renvoyer la liste de tous les livres de la bibliothèque.

def all_livres(request):
    livres = Livre.objects.all()
    return render(request, "livres.html", {'livres': livres})


# b) Afficher les détails d'un étudiant particulier

def get_student(request, id):
    student = Etudiant.objects.all().get(id=id)
    return render(request, 'etudiant.html', {'etudiant': student})


# c) Chercher un livre par leur ISBN

def get_livre_par_isbn(request, isbn):
    livre = Livre.objects.all().get(isbn=isbn)
    return render(request, 'user.html', {'livre': livre})


# d) Obtenir un emprunt (cette méthode prend en paramètre id du livre souhaité, vérifie la disponibilité du livre
# ainsi si numOuvrage emprunté par l’étudiant connecté est inférieur à 5 livres)
# NB. date_de_sortie est la date d’obtention de l’emprunte, date_de_retour est date_de_sortie + 14 jours

def get__emprunt(request, id_livre):
    livre = Livre.objects.all().get(id=id_livre)
    etudiant = Etudiant.objects.get(id=request.user.id)
    if livre.disponible and etudiant.numOuvrage < 5:
        date_de_sortie = timezone.now().date()
        date_de_retour = date_de_sortie + timedelta(days=14)

        emprunt = Emprunteur(
            date_de_sortie=date_de_sortie,
            date_de_retour=date_de_retour,
            etudiant=etudiant,
            livre=livre
        )
        emprunt.save()
        return emprunt
    else:
        return None

# question c
# 1- Ajouter 'django.contrib.auth' dans la liste INSTALLED_APPS de votre fichier settings.py

# 2- Exécuter la commande python manage.py migrate pour appliquer les migrations nécessaires à la création des tables d'authentification dans la base de données.

# 3- Configurer les URL pour l'authentification dans votre fichier urls.py

# 4- Configurer les paramètres d'authentification dans votre fichier settings.py. Vous pouvez spécifier la vue de connexion par défaut et la page vers laquelle rediriger après la connexion ou la déconnexion :

# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'login'

# 5- Utiliser les décorateurs fournis par "django.contrib.auth.decorators" ==> "@login_required"  pour protéger les vues nécessitant une authentification.
