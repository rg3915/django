from django.db import models
#from django.contrib.auth.models import User

# class userProfile(models.Model):
# 	def url(self,filename):
# 		ruta = "MultimediaData/Users/%s/%s"%(self.username,filename)
# 		return ruta

# 	user = models.OneToOneField(User)
# 	photo = models.ImageField(upload_to=url)
# 	fone = models.CharField(max_length=30)

# 	def __unicode__(self):
# 		return self.user.username

class CategoriaProduto(models.Model):
	nome = models.CharField(max_length=200)
	apelido = models.CharField(max_length=200)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		nomeCompleto = "%s %s"%(self.nome,self.apelido)
		return nomeCompleto

class Produto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Produto/%s/%s"%(self.nome,str(filename))
		return ruta

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px height=50px/></a>'%(self.imagem,self.imagem)

	thumbnail.allow_tags = True

	nome = models.CharField(max_length=100)
	descricao = models.TextField(max_length=300)
	status = models.BooleanField(default=True)
	imagem = models.ImageField(upload_to=url,null=True,blank=True)
	preco = models.DecimalField(max_digits=6, decimal_places=2)
	estoque = models.IntegerField()
	categorias = models.ManyToManyField(CategoriaProduto,null=True,blank=True)

	def __unicode__(self):
		return self.nome