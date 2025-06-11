from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Reservation

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email' ,'password1', 'password2', ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
class ReservationForm(UserCreationForm):
    class Meta:
        model = Reservation
        fields = ['match', 'equipe']
        widgets = {
            'match': forms.TextInput(attrs={'class': 'form-control'}),
            'equipe': forms.TextInput(attrs={'class': 'form-control'}),
        }
    