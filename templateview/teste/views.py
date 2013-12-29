# encoding: utf-8

from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView, FormView
#from django.views.generic.edit import FormView

from teste.models import Contato
from teste.forms import ContatoForm

def index(request):
	return render_to_response('teste/index.html')

class index2(TemplateView):
	template_name = 'teste/index2.html'

class Lista(ListView):
	template_name = 'teste/lista.html'
	model = Contato
	context_object_name = 'nomes'

class Criar(FormView):
	template_name = 'teste/formulario.html'
	form_class = ContatoForm
	success_url = '/'

	def form_valid(self, form):
		print(self.request.POST['nome'])
		return super(Criar, self).form_valid(form)
