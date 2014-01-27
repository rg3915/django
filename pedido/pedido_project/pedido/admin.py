# encoding: utf-8
from pedido.models import *
from django.contrib import admin

admin.site.register((Cliente, Pedido, DetPedido, Produto, Categoria))