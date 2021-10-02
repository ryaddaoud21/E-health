from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class MedcinForm(forms.ModelForm):
    class Meta:
        model = Médcin
        fields = '__all__'


class AssistantForm(forms.ModelForm):

    class Meta:
        model = Assistant
        fields = '__all__'



class PatForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'



class SalleForm(forms.ModelForm):

    class Meta:
        model = Salle
        fields = ['Nemero_salle','Numero_lits', 'Etage', 'complete',]

class MaterielForm(forms.ModelForm):

    class Meta:
        model = Ressource_Materiel
        fields = ['type','quantié', ]


class HospitalisationForm(forms.ModelForm):

    class Meta:
        model =Hospitalisation
        fields ='__all__'
