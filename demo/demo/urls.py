# encoding: utf-8

from django.conf.urls import patterns, include, url
from home.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index.as_view(), name='home'),
    # url(r'^demo/', include('demo.foo.urls')),
)
