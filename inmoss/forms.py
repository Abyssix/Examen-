from django import forms
from .models import Casa
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['ubicacion', 'precio', 'disponibilidad', 'imagen']
        widgets = {
            'precio': forms.NumberInput(attrs={'min': '0', 'step': '0.01'}),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
