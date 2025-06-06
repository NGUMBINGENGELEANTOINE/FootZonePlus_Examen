from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from FootZonePlusApp.forms import SignupForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def profilUser(request):
    return render(request, 'MonProfil.html')

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