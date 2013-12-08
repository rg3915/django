# -*- encoding: utf-8 -*-

from django import forms
from models import Carros

class FormCarro(forms.ModelForm):
	class Meta:
		model = Carros