from django.conf.urls import patterns, url
from encurtador.views import LinkCreate, LinkShow

urlpatterns = patterns('',
                       url(r'^$', LinkCreate.as_view(), name='home'),
                       url(r'^link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'))
