from django.contrib import admin
from home.models import *
#from home.models import userProfile

#admin.site.register(userProfile)
admin.site.register((Produto, CategoriaProduto))