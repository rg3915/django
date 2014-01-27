# encoding: utf-8
from vendas.models import *
from django.contrib import admin

admin.site.register((Cliente, Venda, DetVenda, Produto, Categoria))