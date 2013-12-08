# -*- coding: utf-8 -*-   
from django.db import models

class marcas(models.Model):
	marca = models.CharField('Marca', max_length=50)

	class Meta:
		verbose_name=u'marca'
		verbose_name_plural=u'marcas'

	def __unicode__(self):
		return self.marca

class modelos(models.Model):
	modelo = models.CharField('Modelo', max_length=50)
	marca = models.ForeignKey(marcas)

	class Meta:
		verbose_name=u'modelo'
		verbose_name_plural=u'modelos'

	def __unicode__(self):
		return self.modelo

class Carros(models.Model):
	veiculo = models.CharField('Veículo',max_length=50)
	modelo = models.ForeignKey(modelos	)
	preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

	class Meta:
		verbose_name=u'carro' 
		verbose_name_plural=u'carros'   

	def __unicode__(self):
		return self.veiculo