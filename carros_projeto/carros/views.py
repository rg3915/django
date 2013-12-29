# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from carros.models import *
from carros.forms import *

def indexView(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def backOffice(request):
	return render_to_response('back_office.html',context_instance=RequestContext(request))

def listaMarca(request):
	lista_itens = Marca.objects.all()
	return render_to_response('lista_marca.html', {'marcas': lista_itens},
		context_instance=RequestContext(request))

def listaModelo(request):
	lista_itens = Modelo.objects.all()
	return render_to_response('lista_modelo.html', {'modelos': lista_itens},
		context_instance=RequestContext(request))

def listaVeiculo(request):
	lista_itens = Veiculo.objects.all()
	return render_to_response('lista_veiculo.html', {'veiculos': lista_itens},
		context_instance=RequestContext(request))

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

def adicionaVeiculo(request):
	info_enviado = False
	if request.method == 'POST':
		form = FormVeiculo(request.POST, request.FILES)
		if form.is_valid():
			info_enviado = True
			form.save()
			# return render_to_response("salvo.html", {})
	else:
		form = FormVeiculo()
	ctx = {'form': form, 'info_enviado':info_enviado}
	return render_to_response("adiciona_veiculo.html", ctx,
		context_instance=RequestContext(request))

