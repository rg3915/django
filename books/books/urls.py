from django.conf.urls import patterns, include, url
from booksite.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'booksite.views',
    # url(r'^$', 'home', name='home'),
    url(r'^$', AddAuthorView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^managebooks/(?P<author_id>\d+)/$', 'manage_books', name='manage_books')
    url(r'^admin/', include(admin.site.urls)),
)
