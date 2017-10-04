from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^detalhes/(?P<slug>[\w_-]+)/$', views.details, name='details')
]
