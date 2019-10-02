from django.forms import ModelForm
from Questions.models import Personal, Empresa
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = ['company','position', 'initial', 'finish']
        labels = {
            'company': 'Empresa',
            'position': 'Cargo',
            'initial': 'Fecha de inicio',
            'finish': 'Fecha de termino'
        }
        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'initial': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Fecha', 'type': 'date'}),
            'finish': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Fecha', 'type': 'date'})
        }


class UserForm(ModelForm):
    password1 = forms.CharField(help_text=None, label='Ingrese contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de usuario'}),
        }

class CompanyForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['name','n_workers']
        labels = {
            'name': 'Nombre',
            'n_workers': 'Número de trabajadores'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese nombre de la empresa'}),
            'n_workers': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese cantidad de trabajadores'})
        }