from django.shortcuts import render_to_response
from carros.models import Carro

def index(request):
	return render_to_response('carros/index.html',{
		'carros': Carro.objects.all().order_by('id')
		})