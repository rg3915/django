# encoding: utf-8
from django.conf.urls import patterns, include, url
from pedido.views import *
from pedido.models import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'pedido_project.views.home', name='home'),
    url(r'^$', index.as_view(), name='home'),
    url(r'^lista_produto/$', listaProduto.as_view(), name='lista_produto'),
)
