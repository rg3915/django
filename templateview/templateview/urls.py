# encoding: utf-8

from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

from teste.views import *
from teste.models import Contato
from teste.forms import ContatoForm

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', TemplateView.as_view(template_name='teste/index.html')),
	url(r'^index2/$', index2.as_view()),
	url(r'^lista/$', Lista.as_view()),
	url(r'^formulario/$', Criar.as_view()),
	#url(r'lista_marca/$', 'carros.views.listaMarca', name='lista_marca'),
)
