from django import forms
from models import Contato

class ContatoForm(forms.ModelForm):
	email = forms.CharField(max_length=50) # campo extra no formulario

	class Meta:
		model = Contato