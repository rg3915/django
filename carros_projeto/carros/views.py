# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from carros.models import Carros
from carros.forms import FormCarro

#def index(request):
#	return render_to_response('index.html',{
#		'carros': Carro.objects.all().order_by('id')
#		})

def lista(request):
	lista_itens = Carros.objects.all()
	return render_to_response('lista.html', {'carros': lista_itens},
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

def item(request, nr_item):
	item = get_object_or_404(Carro, pk=nr_item)
	return render_to_response("item.html", {'item': item},
		context_instance=RequestContext(request))

