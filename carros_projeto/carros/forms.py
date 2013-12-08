# -*- encoding: utf-8 -*-

from django import forms
from models import *

class FormCarro(forms.ModelForm):
	class Meta:
		model = Carros

class FormMarca(forms.ModelForm):
	class Meta:
		model = marcas

class FormModelo(forms.ModelForm):
	class Meta:
		model = modelos