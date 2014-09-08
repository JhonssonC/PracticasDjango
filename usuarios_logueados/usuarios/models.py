from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models

# Create your models here.

#EDICION DE MODELO USER
User.add_to_class('usuarioSico', models.CharField(max_length=10, null=False, blank=False))
User.add_to_class('contraseniaSico', models.CharField(max_length=10, null=False, blank=False))
#User.add_to_class('amigos', models.ManyToManyField('self', symmetrical=True,  blank=True))

#FORMULARIOS
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'usuarioSico', 'contraseniaSico']
        widgets = {
            'password': forms.PasswordInput(),
        }
