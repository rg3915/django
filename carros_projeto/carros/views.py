# encoding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import login,logout,authenticate
from carros.models import *
from carros.forms import *

class index(TemplateView):
	template_name = 'index.html'

class backOffice(TemplateView):
	template_name = 'back_office.html'

class listaMarca(ListView):
	template_name = 'lista_marca.html'
	model = Marca
	context_object_name = 'marcas'
	#lista_itens = Marca.objects.all()
	#return render_to_response('lista_marca.html', {'marcas': lista_itens},
	#	context_instance=RequestContext(request))

class listaModelo(ListView):
	template_name = 'lista_modelo.html'
	model = Modelo
	context_object_name = 'modelos'

class listaVeiculo(ListView):
	template_name = 'lista_veiculo.html'
	model = Veiculo
	context_object_name = 'veiculo'

def itemMarca(request, nr_item):
	item = get_object_or_404(Marca, pk=nr_item)
	return render_to_response("item_marca.html", {'item_marca': item},
		context_instance=RequestContext(request))

def itemModelo(request, nr_item):
	item = get_object_or_404(Modelo, pk=nr_item)
	return render_to_response("item_modelo.html", {'item_modelo': item},
		context_instance=RequestContext(request))

def itemVeiculo(request, nr_item):
	item = get_object_or_404(Veiculo, pk=nr_item)
	return render_to_response("item_veiculo.html", {'item_veiculo': item},
		context_instance=RequestContext(request))

def adicionaMarca(request):
	info_enviado = False
	if request.method == 'POST':
		form = FormMarca(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			form.save()

			# enviando email - apenas teste
			#to_admin = 'regis.santos.100@gmail.com'
			#html_content = "Informação recebida"
			#msg = EmailMultiAlternatives('Correio de contato',html_content,'from@server.com',[to_admin])
			#msg.attach_alternative(html_content, 'text/html')
			#msg.send()
	else:
		form = FormMarca()
	ctx = {'form': form, 'info_enviado':info_enviado}
	return render_to_response("adiciona_marca.html", ctx,
		context_instance=RequestContext(request))

def adicionaModelo(request):
	info_enviado = False
	if request.method == 'POST':
		form = FormModelo(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			form.save()
	else:
		form = FormModelo()
	ctx = {'form': form, 'info_enviado':info_enviado}
	return render_to_response("adiciona_modelo.html", ctx,
		context_instance=RequestContext(request))

class adicionaVeiculo(CreateView):
	info_enviado = False
	template_name = 'adiciona_veiculo.html'
	model = Veiculo
	success_url = 'adiciona_veiculo'

	def form_valid(self, form):
		self.info_enviado = True
		return super(adicionaVeiculo, self).form_valid(form)

	def get_context_data(self, **kwargs):
		ctx = super(adicionaVeiculo, self).get_context_data(**kwargs)
		ctx['info_enviado'] = self.info_enviado
		return ctx

	# info_enviado = False
	# if request.method == 'POST':
	# 	form = FormVeiculo(request.POST, request.FILES)
	# 	if form.is_valid():
	# 		info_enviado = True
	# 		form.save()
	# 		# return render_to_response("salvo.html", {})
	# else:
	# 	form = FormVeiculo()
	# ctx = {'form': form, 'info_enviado':info_enviado}
	# return render_to_response("adiciona_veiculo.html", ctx,
	# 	context_instance=RequestContext(request))

def login_view(request):
	mensagem = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['Nome']
				password = form.cleaned_data['Senha']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensagem = "Usuario e/ou senha incorreta."
	form = LoginForm()
	ctx = {'form':form,'mensagem':mensagem}
	return render_to_response("login.html",ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')