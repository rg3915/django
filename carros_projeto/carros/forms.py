# -*- encoding: utf-8 -*-

from django import forms
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