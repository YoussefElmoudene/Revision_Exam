from django.shortcuts import render

from exam_principal.models import User


# Create your views here.

def _save():
    User.objects.create(nom='AMEKSA', prenom='Yahya', email='yahya.ameksa@emsi.ma')

