# encoding: utf-8

from django.conf.urls import patterns, include, url
from carros.views import *
from carros.models import *
from carros.forms import *

import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^$', index.as_view(), name='home'),
    #url(r'^$', 'carros.views.indexView', name='home'),
    url(r'back_office/$', 'carros.views.backOffice', name='back_office'),
    url(r'lista_veiculo/$', 'carros.views.listaVeiculo', name='lista_veiculo'),
    url(r'item_veiculo/(?P<nr_item>\d+)/$', 'carros.views.itemVeiculo', name='item_veiculo'),
    url(r'adiciona_veiculo/$', 'carros.views.adicionaVeiculo', name='adiciona_veiculo'),
    url(r'lista_marca/$', 'carros.views.listaMarca', name='lista_marca'),
    url(r'item_marca/(?P<nr_item>\d+)/$', 'carros.views.itemMarca', name='item_marca'),
    url(r'adiciona_marca/$', 'carros.views.adicionaMarca', name='adiciona_marca'),
    url(r'lista_modelo/$', 'carros.views.listaModelo', name='lista_modelo'),
    url(r'item_modelo/(?P<nr_item>\d+)/$', 'carros.views.itemModelo', name='item_modelo'),
    url(r'adiciona_modelo/$', 'carros.views.adicionaModelo', name='adiciona_modelo'),
)
