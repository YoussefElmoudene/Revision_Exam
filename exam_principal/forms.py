from django import forms
from django.shortcuts import render

from exam_principal.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model: User
        fields = ['nom', 'prenom', 'email']


def get_user_form(request):
    context = {'UserForm', UserForm()}
    return render(request, 'user.html', context)
