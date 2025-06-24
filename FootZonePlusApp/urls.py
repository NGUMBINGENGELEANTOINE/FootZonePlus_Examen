from django import views
from django.conf import settings
from django.urls import path
from FootZonePlusApp.views import index, profilUser, connexion, register, deconnexion, reservationBillet, contact, apropos, match
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('profil/', profilUser, name="profil"),
    path('connexion/', connexion, name="connexion"),
    path('register/', register, name="register"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('reservation/', reservationBillet, name="reservation"),
    path('contact/', contact, name="contact"),
    path('apropos/', apropos, name="apropos"),
    path('match/', match, name="match"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
