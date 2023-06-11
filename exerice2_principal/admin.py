from django.contrib import admin

from exerice2_principal.models import Etudiant, Livre


@admin.register(Etudiant)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'cne')
    ordering = ('level',)
    list_filter = ('numOuvrage',)
    search_fields = ('level',)


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'numCopies', 'disponible')
    ordering = ('numCopies',)
