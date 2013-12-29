from django import forms
from models import Contato
#from django.contrib.auth.forms import UserCreationForm

#class ContatoForm(UserCreationForm):
class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato