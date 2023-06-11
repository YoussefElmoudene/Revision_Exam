from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Etudiant(User):
    nom = models.CharField(),
    prenom = models.CharField(),
    filiere = models.CharField(),
    numTel = models.BigIntegerField(),
    email = models.EmailField(),
    numOuvrage = models.IntegerField(),
    cne = models.CharField()


class Livre(models.Model):
    titre = models.CharField(),
    auteur = models.CharField(),
    resume = models.CharField(),
    isbn = models.CharField(),
    numCopies = models.IntegerField(),
    disponible = models.BooleanField(default=True)


class Emprunteur(models.Model):
    date_de_sortie = models.DateField,
    date_de_retour = models.DateField,
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

# after this use

# ##py manage.py makemigrations => pour

# #then

# ## py manage.py migrate

# pour connecter a interface shell => python manage.py shell

# from exerice2_principal.models import Etudiant, Livre, Emprunteur

# ----------- CREATION DE STUDENT --------------------------
# etudiant = Etudiant(nom="Nom de l'étudiant", prenom="Prénom de l'étudiant", filiere="Filière de l'étudiant", numTel=123456789, email="email@exemple.com", numOuvrage=5, cne="CNE de l'étudiant")
# etudiant.save()


# ----------- CREATION DE LIVRE --------------------------

# livre = Livre(titre="Titre du livre", auteur="Auteur du livre", resume="Résumé du livre", isbn="ISBN du livre", numCopies=10, disponible=True)
# livre.save()

# ----------- CREATION DE EMPRUNTEUR --------------------------

# emprunteur = Emprunteur(date_de_sortie="2023-06-11", date_de_retour="2023-06-18", etudiant=etudiant, livre=livre)
# emprunteur.save()
