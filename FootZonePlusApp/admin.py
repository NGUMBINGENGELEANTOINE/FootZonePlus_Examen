from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FootZonePlusApp.models import CustomUser, Place, Match, Reservation, PlaceReservee

# Register your models here.

# class AdminContinent(admin.ModelAdmin):
#     list_display= ('id','nom', 'date_time_add')

# class AdminPaiement(admin.ModelAdmin):
#     list_display= ('id','utilisateur','match', 'montant', 'date_paiement', 'moyen_paiement', 'statut')

# class AdminPays(admin.ModelAdmin):
#     list_display= ('id','nom', 'continent', 'date_time_add')

class AdminPlace(admin.ModelAdmin):
    list_display= ('id','match', 'rangée', 'numéro', 'type', 'prix', 'est_disponible', 'date_time_add')

# class AdminCategorie_Equipe(admin.ModelAdmin):
#     list_display= ('id','titre', 'date_time_add')

# class AdminCategorie_Match(admin.ModelAdmin):
#     list_display= ('id','titre', 'date_time_add')

# class AdminEquipe(admin.ModelAdmin):
#     list_display= ('id','nom', 'categorie', 'coatch', 'nombre_joueur', 'pays_origine', 'date_time_add')

# class AdminEquipeVisiteuse(admin.ModelAdmin):
#     list_display= ('id','nom', 'categorie', 'coatch', 'nombre_joueur', 'pays_origine', 'date_time_add')

# class AdminStade(admin.ModelAdmin):
#     list_display= ('id','nom', 'pays', 'nombre_place', 'adresse', 'date_time_add')
    
class AdminMatch(admin.ModelAdmin):
    list_display= ('id', 'image', 'equipe_locale', 'equipe_visiteuse', 'date_heure', 'lieu', 'status', 'date_time_add')

class AdminReservation(admin.ModelAdmin):
    list_display= ('id','utilisateur', 'match', 'date_reservation', 'total','statut')

class AdminPlaceReservee(admin.ModelAdmin):
    list_display= ('id','reservation','place')


admin.site.register(CustomUser, UserAdmin)
# admin.site.register(Continent, AdminContinent)
# admin.site.register(Paiement, AdminPaiement)
# admin.site.register(Pays, AdminPays)
admin.site.register(Place, AdminPlace)
# admin.site.register(Categorie_Equipe, AdminCategorie_Equipe)
# admin.site.register(Categorie_Match, AdminCategorie_Match)
# admin.site.register(Equipe, AdminEquipe)
# admin.site.register(EquipeVisiteuse, AdminEquipeVisiteuse)
# admin.site.register(Stade, AdminStade)
admin.site.register(Match, AdminMatch)
admin.site.register(Reservation, AdminReservation)
admin.site.register(PlaceReservee, AdminPlaceReservee)
