from django.conf.urls import patterns, include, url
from booksite.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'booksite.views',
    url(r'^$', 'authors_list'),
    url(r'^author/add/$', 'author_add'),
    url(r'^author/edit/(?P<pk>\d+)$', 'author_edit'),
    url(r'^author/delete/(?P<pk>\d+)$', 'author_delete'),
    url(r'^admin/', include(admin.site.urls)),
)
