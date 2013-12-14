# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from carros.models import *
from carros.forms import *

def index_view(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def lista(request):
	lista_itens = Carros.objects.all()
	return render_to_response('lista.html', {'carros': lista_itens},
		context_instance=RequestContext(request))

def listaMarca(request):
	lista_itens = marcas.objects.all()
	return render_to_response('listamarca.html', {'marcas': lista_itens},
		context_instance=RequestContext(request))

def listaModelo(request):
	lista_itens = modelos.objects.all()
	return render_to_response('listamodelo.html', {'modelos': lista_itens},
		context_instance=RequestContext(request))

def adiciona(request):
	if request.method == 'POST':
		form = FormCarro(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormCarro()
	return render_to_response("adiciona.html", {'form': form},
		context_instance=RequestContext(request))

def adicionaMarca(request):
	if request.method == 'POST':
		form = FormMarca(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvomarca.html", {})
	else:
		form = FormMarca()
	return render_to_response("adicionamarca.html", {'form': form},
		context_instance=RequestContext(request))

def adicionaModelo(request):
	if request.method == 'POST':
		form = FormModelo(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormModelo()
	return render_to_response("adicionamodelo.html", {'form': form},
		context_instance=RequestContext(request))

def item(request, nr_item):
	item = get_object_or_404(Carro, pk=nr_item)
	return render_to_response("item.html", {'item': item},
		context_instance=RequestContext(request))

def itemMarca(request, nr_item):
	item = get_object_or_404(marca, pk=nr_item)
	return render_to_response("itemmarca.html", {'item': item},
		context_instance=RequestContext(request))

