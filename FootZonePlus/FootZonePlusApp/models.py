from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.contrib.auth import get_user_model

from FootZonePlus import settings

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Le nom d'utilisateur est requis")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_client = True  # Par défaut
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_client", False)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Le superutilisateur doit avoir is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Le superutilisateur doit avoir is_superuser=True.")
        return self.create_user(username, email, password, **extra_fields)



class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=True)

    objects = CustomUserManager()

class Continent(models.Model):
    nom = models.CharField(max_length=100)
    date_time_add = models.DateTimeField(auto_now_add=True)

class Pays(models.Model):
    nom = models.CharField(max_length=100)
    date_time_add = models.DateTimeField(auto_now_add=True)

class Categorie_Equipe(models.Model):
    titre = models.CharField(max_length=200, default='Club')
    date_time_add = models.DateTimeField(auto_now_add=True)

class Categorie_Match(models.Model):
    titre = models.CharField(max_length=200, default='Match amical')
    date_time_add = models.DateTimeField(auto_now_add=True)

class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie_Equipe, on_delete=models.CASCADE, null=True)
    coatch = models.CharField(max_length=100)
    nombre_joueur = models.IntegerField()
    pays_origine = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True)
    date_time_add = models.DateTimeField(auto_now_add=True)

class Stade(models.Model):
    nom = models.CharField(max_length=200)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True)
    nombre_place = models.IntegerField()
    adresse = models.TextField()
    date_time_add = models.DateTimeField(auto_now_add=True)

class Match(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True)
    categorie = models.ForeignKey(Categorie_Match, on_delete=models.CASCADE, null=True)
    equipe_locale = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True)
    equipe_visiteuse = models.CharField(max_length=100)
    stade = models.ForeignKey(Stade, on_delete=models.CASCADE, null=True)
    date_heure = models.DateTimeField()
    status = models.CharField(max_length=50 ,choices=[('Ouvert', 'Ouvert'), ('Fermé', 'Fermé')])
    description = models.TextField()
    date_time_add = models.DateTimeField(auto_now_add=True)

class Place(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    rangée = models.CharField(max_length=10)
    numéro = models.IntegerField()
    type = models.CharField(max_length=20, choices=[('VIP', 'VIP'), ('VVIP', 'VVIP'), ('Standard', 'Standard')])
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    est_disponible = models.BooleanField(default=True)
    date_time_add = models.DateTimeField(auto_now_add=True)

class Reservation(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, default='confirmée')

class PlaceReservee(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='places', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

class Paiement(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    moyen_paiement = models.CharField(max_length=50)
    statut = models.CharField(max_length=20, choices=[('Validé', 'Validé'), ('En attente', 'En attente'), ('Annulé', 'Annulé')])

