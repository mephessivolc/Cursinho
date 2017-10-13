from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^inserir/$', views.insert, name='insert'),
    url(r'^(?P<slug>[\w_-]+)/detalhes/$', views.details, name='details'),
    url(r'^entrar/$', auth_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout,
        {'next_page': 'accounts:login'}, name='logout'),

]


# 'template_name': 'accounts/login.html', 'next_page': '/'

# 'next_page': 'accounts/login.html'
