# encoding: utf-8
from django.db import models
from datetime import date

class Cliente(models.Model):
	cpf = models.CharField('CPF', max_length=11)
	nome = models.CharField('Nome', max_length=50)
	sobrenome = models.CharField('Sobrenome', max_length=50)
	email = models.CharField('e-mail', max_length=50)
	fone = models.CharField('Fone', max_length=50)

	class Meta:
		verbose_name=u'cliente'
		verbose_name_plural=u'clientes'

	def __unicode__(self):
		return self.cpf

class Categoria(models.Model):
	categoria = models.CharField('Categoria', max_length=50)

	class Meta:
		verbose_name=u'categoria'
		verbose_name_plural=u'categorias'

	def __unicode__(self):
		return self.categoria

class Produto(models.Model):
	def url(self,filename):
		caminho = "static/produto/%s/%s"%(self.produto,str(filename))
		return caminho

	importado = models.BooleanField('Importado',default=False)
	foradelinha = models.BooleanField('Fora de linha',default=False)
	categoria = models.ForeignKey(Categoria)
	produto = models.CharField('Produto', max_length=50)
	preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
	imagem = models.ImageField('Imagem', upload_to=url, null=True, blank=True)

	class Meta:
		verbose_name=u'produto'
		verbose_name_plural=u'produtos'

	def __unicode__(self):
		return self.produto

class Venda(models.Model):
	datavenda = models.DateField('Data da venda')
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return unicode(self.datavenda)

class DetVenda(models.Model):
	venda = models.ForeignKey(Venda)
	produto = models.ForeignKey(Produto)
	quantidade = models.IntegerField()
	precovenda = models.DecimalField('Preço de venda', max_digits=8, decimal_places=2)

	def __unicode__(self):
		return unicode(self.venda)
