# encoding: utf-8

from django.db import models

class Contato(models.Model):
	nome = models.CharField(max_length=50)
	sobrenome = models.CharField(max_length=50)
	idade = models.IntegerField()

	def __unicode__(self):
		return self.nome