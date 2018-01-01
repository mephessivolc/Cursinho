from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^inserir/$', views.insert, name='insert'),
    url(r'^(?P<slug>[\w_-]+)/detalhes/$', views.details, name='details'),
]
