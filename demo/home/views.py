# encoding: utf-8

from django.views.generic import TemplateView
from home.models import *

class index(TemplateView):
	template_name = 'home/index.html'