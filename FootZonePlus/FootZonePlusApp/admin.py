from django.contrib import admin

from FootZonePlusApp.models import Continent, Utilisateur, Paiement, Pays, Place, PlaceReservee, Categorie_Equipe, Categorie_Match, Equipe, Stade, Match, Reservation

# Register your models here.

class AdminContinent(admin.ModelAdmin):
    list_display= ('nom', 'date_time_add')

class AdminPaiement(admin.ModelAdmin):
    list_display= ('reservation', 'montant', 'date_paiement', 'moyen_paiement', 'statut')

class AdminPays(admin.ModelAdmin):
    list_display= ('nom', 'date_time_add')

class AdminPlace(admin.ModelAdmin):
    list_display= ('match', 'rangée', 'numéro', 'type', 'prix', 'est_disponible', 'date_time_add')

class AdminPlaceReservee(admin.ModelAdmin):
    list_display= ('reservation', 'place')

class AdminCategorie_Equipe(admin.ModelAdmin):
    list_display= ('titre', 'date_time_add')

class AdminCategorie_Match(admin.ModelAdmin):
    list_display= ('titre', 'date_time_add')

class AdminEquipe(admin.ModelAdmin):
    list_display= ('nom', 'categorie', 'coatch', 'nombre_joueur', 'pays_origine', 'date_time_add')

class AdminStade(admin.ModelAdmin):
    list_display= ('nom', 'pays', 'nombre_place', 'adresse', 'date_time_add')
    
class AdminMatch(admin.ModelAdmin):
    list_display= ('continent', 'categorie', 'equipe_locale', 'equipe_visiteuse', 'stade', 'date_heure', 'status', 'description', 'date_time_add')

class AdminReservation(admin.ModelAdmin):
    list_display= ('utilisateur', 'match', 'date_reservation', 'total', 'statut')


admin.site.register(Utilisateur)
admin.site.register(Continent, AdminContinent)
admin.site.register(Paiement, AdminPaiement)
admin.site.register(Pays, AdminPays)
admin.site.register(Place, AdminPlace)
admin.site.register(PlaceReservee, AdminPlaceReservee)
admin.site.register(Categorie_Equipe, AdminCategorie_Equipe)
admin.site.register(Categorie_Match, AdminCategorie_Match)
admin.site.register(Equipe, AdminEquipe)
admin.site.register(Stade, AdminStade)
admin.site.register(Match, AdminMatch)
admin.site.register(Reservation, AdminReservation)