from django import views
from django.urls import path
from FootZonePlusApp.views import index, profilUser, connexion, register, deconnexion, reservationBillet


urlpatterns = [
    path('', index, name="index"),
    path('profil/', profilUser, name="profil"),
    path('connexion/', connexion, name="connexion"),
    path('register/', register, name="register"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('reservation/', reservationBillet, name="reservation")
]