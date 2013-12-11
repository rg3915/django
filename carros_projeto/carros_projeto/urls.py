from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carros_projeto.views.home', name='home'),
    # url(r'^carros_projeto/', include('carros_projeto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'carros.views.lista'),
    url(r'adiciona/$', 'carros.views.adiciona'),
    url(r'item/(?P<nr_item>\d+)/$', 'carros.views.item'),
    url(r'listamarca/$', 'carros.views.listaMarca'),
    url(r'adicionamarca/$', 'carros.views.adicionaMarca'),
    url(r'adicionamodelo/$', 'carros.views.adicionaModelo'),
)
