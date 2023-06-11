from django.db import models
from django import forms


# Create user model.

class User(models.Model):
    nom = models.CharField(max_length=50),
    prenom = models.CharField(max_length=50),
    email = models.EmailField(),
    is_active = models.BooleanField(default=True)
