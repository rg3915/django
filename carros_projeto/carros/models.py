# -*- coding: utf-8 -*-   

from django.db import models

class Carro(models.Model):
	marca = models.CharField('Marca',max_length=50)
	modelo = models.CharField('Modelo',max_length=50)
	veiculo = models.CharField('Veículo',max_length=50)
	preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

	class Meta:
		verbose_name = 'carro' 
		verbose_name_plural = 'carros'   

	def __unicode__(self):
		return self.veiculo