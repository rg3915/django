# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from models import *

class FormVeiculo(forms.ModelForm):
	class Meta:
		model = Veiculo

class FormMarca(forms.ModelForm):
	class Meta:
		model = Marca

class FormModelo(forms.ModelForm):
	class Meta:
		model = Modelo

class LoginForm(forms.Form):
	Usuario = forms.CharField(label='Usuário',widget=forms.TextInput())
	Senha = forms.CharField(widget=forms.PasswordInput(render_value=False))