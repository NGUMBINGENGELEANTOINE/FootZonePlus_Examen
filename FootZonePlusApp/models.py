from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.contrib.auth import get_user_model



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

# class Continent(models.Model):
#     nom = models.CharField(max_length=100)
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nom

# class Pays(models.Model):
#     nom = models.CharField(max_length=100)
#     continent = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True)
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nom

# class Categorie_Equipe(models.Model):
#     titre = models.CharField(max_length=200, default='Club')
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.titre

# class Categorie_Match(models.Model):
#     titre = models.CharField(max_length=200, default='Match amical')
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.titre

# class Equipe(models.Model):
#     nom = models.CharField(max_length=100)
#     categorie = models.ForeignKey(Categorie_Equipe, on_delete=models.CASCADE, null=True)
#     coatch = models.CharField(max_length=100)
#     nombre_joueur = models.IntegerField()
#     pays_origine = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True)
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nom
    
# class EquipeVisiteuse(models.Model):
#     nom = models.CharField(max_length=100)
#     categorie = models.ForeignKey(Categorie_Equipe, on_delete=models.CASCADE, null=True)
#     coatch = models.CharField(max_length=100)
#     nombre_joueur = models.IntegerField()
#     pays_origine = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True)
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nom

# class Stade(models.Model):
#     nom = models.CharField(max_length=200)
#     pays = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True)
#     nombre_place = models.IntegerField()
#     adresse = models.TextField()
#     date_time_add = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nom

class Match(models.Model):
    # continent = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True)
    # categorie = models.ForeignKey(Categorie_Match, on_delete=models.CASCADE, null=True)
    # equipe_locale = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True)
    # equipe_visiteuse = models.ForeignKey(EquipeVisiteuse, on_delete=models.CASCADE,related_name="Equipe_Visiteuse", null=True)
    # stade = models.ForeignKey(Stade, on_delete=models.CASCADE, null=True)
    equipe_locale = models.CharField(max_length=100, null=True)
    equipe_visiteuse = models.CharField(max_length=100, null=True)
    date_heure = models.DateTimeField(null=True)
    lieu = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=50 ,choices=[('Ouvert', 'Ouvert'), ('Fermé', 'Fermé')], null=True)
    date_time_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.equipe_locale 

class Place(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    rangée = models.CharField(max_length=10, null=True)
    numéro = models.IntegerField(null=True)
    type = models.CharField(max_length=20, null=True)
    prix = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    est_disponible = models.BooleanField(default=True)
    date_time_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


# class Paiement(models.Model):
#     utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
#     montant = models.DecimalField(max_digits=10, decimal_places=2)
#     date_paiement = models.DateTimeField(auto_now_add=True)
#     moyen_paiement = models.CharField(max_length=50)
#     statut = models.CharField(max_length=20, choices=[('Validé', 'Validé'), ('En attente', 'En attente'), ('Annulé', 'Annulé')])

class Reservation(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    statut = models.CharField(max_length=20, null=True)

class PlaceReservee(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
