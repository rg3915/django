# encoding: utf-8
from django.views.generic import TemplateView, ListView
from pedido.models import *

class index(TemplateView):
	template_name = 'pedido/index.html'

class listaProduto(ListView):
	template_name = 'pedido/lista_produto.html'
	model = Produto
	context_object_name = 'produtos'