# encoding: utf-8

from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView
#from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView

from teste.models import Contato
from teste.forms import ContatoForm

def index(request):
	return render_to_response('teste/index.html')

class index2(TemplateView):
	template_name = 'teste/index2.html'

class Lista(ListView):
	template_name = 'teste/lista.html'
	#queryset = Contato.objects.all(),
	model = Contato
	context_object_name = 'nomes'

class Criar(CreateView):
	template_name = 'teste/formulario.html'
	model = Contato
	#form_class = ContatoForm
	success_url = '../lista'

	def form_valid(self, form):
		# user = form.save() # usado com FormView
		print(self.request.POST['sobrenome'])
		return super(Criar, self).form_valid(form)
