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
    url(r'^$', 'carros.views.index_view', name='home'),
    url(r'adiciona/$', 'carros.views.adiciona', name='adiciona_carro'),
    url(r'item/(?P<nr_item>\d+)/$', 'carros.views.item', name='item_carro'),
    url(r'listamarca/$', 'carros.views.listaMarca', name='lista_marca'),
    url(r'adicionamarca/$', 'carros.views.adicionaMarca', name='adiciona_marca'),
    url(r'adicionamodelo/$', 'carros.views.adicionaModelo', name='adiciona_modelo'),
)
