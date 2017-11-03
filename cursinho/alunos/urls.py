from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^inserir/$', views.insert, name='insert'),
    url(r'^(?P<slug>[\w_-]+)/detalhes/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/atualizar/$', views.update, name='update'),
]
