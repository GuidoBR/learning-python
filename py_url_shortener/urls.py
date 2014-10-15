from django.conf.urls import patterns, url
from encurtador.views import LinkCreate

urlpatterns = patterns('',
                       url(r'^$', LinkCreate.as_view(), name='home'))
