# encoding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from teste.views import index2
from teste.models import Contato
from teste.forms import ContatoForm

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='teste/index.html')),
	url(r'^index2/$', index2.as_view()),
	url(r'^lista/$', 'teste.views.Lista'),
	url(r'^formulario/$', 'teste.views.Criar'),
	#url(r'lista_marca/$', 'carros.views.listaMarca', name='lista_marca'),
)
