# -*- coding: utf-8 -*-   
from django.db import models

class Marca(models.Model):
	marca = models.CharField('Marca', max_length=50)

	class Meta:
		verbose_name=u'marca'
		verbose_name_plural=u'marcas'

	def __unicode__(self):
		return self.marca

class Modelo(models.Model):
	modelo = models.CharField('Modelo', max_length=50)
	marca = models.ForeignKey(Marca)

	class Meta:
		verbose_name=u'modelo'
		verbose_name_plural=u'modelos'

	def __unicode__(self):
		return self.modelo

class Veiculo(models.Model):
	veiculo = models.CharField('Veículo',max_length=50)
	modelo = models.ForeignKey(Modelo)
	preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

	class Meta:
		verbose_name=u'veículo' 
		verbose_name_plural=u'veículos'   

	def __unicode__(self):
		return self.veiculo

	def moeda(self):
		p = str(self.preco)
		if p != None:
			import locale
			locale.setlocale( locale.LC_ALL, '')
			return locale.currency( p, grouping=True )
		return ''