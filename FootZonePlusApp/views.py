from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import reserver_meilleure_place

from FootZonePlusApp.models import CustomUser, Reservation, Match, Contact, Apropos
from FootZonePlusApp.forms import SignupForm
from django.db.models import Q


# Create your views here.
def index(request):
    # recherche = request.GET.get('recherche', '')
    # if recherche:
    #     match = Match.objects.filter(
    #         Q(equipe_locale__nom__icontains=recherche) |
    #         Q(equipe_visiteuse__nom__icontains=recherche) |
    #         Q(stade__nom__icontains=recherche) |
    #         Q(categorie__nom__icontains=recherche) |
    #         Q(continent__nom__icontains=recherche)
    #     ).distinct()
    # else:
    match = Match.objects.all()
    return render(request, 'index.html', {'match':match})

@login_required
def profilUser(request):
    reservation = Reservation.objects.all()
    return render(request, 'MonProfil.html', {'user': request.user, 'reservation': reservation})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrecte !")
    return render(request, 'login.html')

# Inscription

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form':form})

def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def reservationBillet(request):
    user = request.user
    reservation = Reservation.objects.filter(utilisateur=user).select_related('match')
    match = Match.objects.all()

    if request.method == 'POST':
        match_id = request.POST.get('match_id')
        type_place = request.POST.getlist('type_place')

        if not match_id or not type_place:
            messages.error(request, "Veuillez sélectionner un match et un type de place.")
            return redirect('profil')
        try:
            reserver_meilleure_place(user, match_id, type_place)
            messages.success(request, "Reservation effectuee avec success!")
        except Exception as e:
            messages.error(request, str(e))
        return redirect('profil')
    return render(request, 'reserverBillet.html', {'reservation': reservation, 'match': match})


def contact(request):
    msg = ''
    if request.method == 'POST':
        form = Contact()
        form.nom =request.POST.get('nom')
        form.prenom = request.POST.get('prenom')
        form.telephone = request.POST.get('phone')
        form.email = request.POST.get('email')
        form.message = request.POST.get('message')

        form.save()
        msg = "Message envoyer avec success!"
    return render(request, 'contact.html', {'msg':msg})

def apropos(request):
    apropos = Apropos.objects.all()
    return render(request, 'apropos.html', {'apropos': apropos})

def match(request):
    match = Match.objects.all()
    return render(request, 'match.html', {'match': match})