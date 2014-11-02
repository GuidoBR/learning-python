from django.conf.urls import patterns, url
from encurtador.views import LinkCreate, LinkShow, RedirectToLongURL

urlpatterns = patterns('',
                       url(r'^$', LinkCreate.as_view(), name='home'),
                       url(r'^r/(?P<short_url>\w+)$',
                           RedirectToLongURL.as_view(),
                           name='redirect_short_url'),
                       url(r'^link/(?P<pk>\d+)$',
                           LinkShow.as_view(), name='link_show'))
