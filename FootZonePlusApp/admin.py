from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FootZonePlusApp.models import Categorie_Equipe, Categorie_Match, Contact, Continent, CustomUser, Equipe, EquipeLocale, EquipeVisiteuse, Pays, Place, Match, Reservation, PlaceReservee, Stade, Apropos
from .pdf_generator import generer_billet_pdf
from django.utils.html import format_html
# Register your models here.

admin.site.site_header = "FootZone+ | Administration"
admin.site.site_title = "FootZone+"
admin.site.index_title = "FootZone+"


class AdminContinent(admin.ModelAdmin):
    list_display= ('id','nom', 'date_time_add')

# class AdminPaiement(admin.ModelAdmin):
#     list_display= ('id','utilisateur','match', 'montant', 'date_paiement', 'moyen_paiement', 'statut')

class AdminPays(admin.ModelAdmin):
    list_display= ('id','nom', 'continent', 'date_time_add')

class AdminPlace(admin.ModelAdmin):
    list_display= ('id','match', 'rangée', 'numéro', 'type', 'prix', 'est_disponible', 'date_time_add')

class AdminCategorie_Equipe(admin.ModelAdmin):
    list_display= ('id','titre', 'date_time_add')

class AdminCategorie_Match(admin.ModelAdmin):
    list_display= ('id','titre', 'date_time_add')

class AdminEquipe(admin.ModelAdmin):
    list_display= ('id','nom', 'categorie', 'coatch', 'nombre_joueur', 'pays_origine', 'date_time_add')

class AdminEquipeVisiteuse(admin.ModelAdmin):
    list_display= ('id','nom', 'categorie', 'coatch', 'nombre_joueur', 'pays_origine', 'date_time_add')

class AdminStade(admin.ModelAdmin):
    list_display= ('id','nom', 'pays', 'nombre_place', 'adresse', 'date_time_add')
    
class AdminMatch(admin.ModelAdmin):
    list_display= ('id', 'continent', 'categorie', 'stade', 'image', 'equipe_locale', 'equipe_visiteuse', 'heure', 'status', 'date')

class AdminReservation(admin.ModelAdmin):
    list_display= ('id','utilisateur', 'match', 'date_reservation', 'total','statut', 'lien_billet')

    def generer_billet_pdf_action(self, request, queryset):
        for reservation in queryset:
            generer_billet_pdf(reservation)
        self.message_user(request, "Billet(s) PDF généré(s) avec succès.")
    generer_billet_pdf_action.short_description = "Générer les billets PDF sélectionnés"

    def lien_billet(self, obj):
        if obj.pdf_file:
            return format_html(f"<a href='{obj.pdf_file.url}' target='_blank'>Télécharger</a>")
        return "Pas encore généré"
    lien_billet.short_description = "Billet PDF"


class AdminPlaceReservee(admin.ModelAdmin):
    list_display= ('id','reservation','place')

class AdminEquipe(admin.ModelAdmin):
    list_display= ('id','nom')

class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'telephone', 'email', 'message')

class AdminApropos(admin.ModelAdmin):
    list_display = ('id', 'image', 'titre', 'slogan', 'contenus')


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Continent, AdminContinent)
admin.site.register(Equipe, AdminEquipe)
admin.site.register(Pays, AdminPays)
admin.site.register(Place, AdminPlace)
admin.site.register(Categorie_Equipe, AdminCategorie_Equipe)
admin.site.register(Categorie_Match, AdminCategorie_Match)
admin.site.register(EquipeLocale, AdminEquipe)
admin.site.register(EquipeVisiteuse, AdminEquipeVisiteuse)
admin.site.register(Stade, AdminStade)
admin.site.register(Match, AdminMatch)
admin.site.register(Reservation, AdminReservation)
admin.site.register(PlaceReservee, AdminPlaceReservee)
admin.site.register(Contact, AdminContact)
admin.site.register(Apropos, AdminApropos)
