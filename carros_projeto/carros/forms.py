# -*- encoding: utf-8 -*-

from django import forms
from models import Carro

class FormCarro(forms.ModelForm):
	class Meta:
		model = Carro