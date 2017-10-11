from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^entrar/$', auth_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout,
        {'next_page': 'core:home'}, name='logout'),
    url(r'^', views.home, name='home'),
    url(r'^inserir/', views.insert, name='insert'),
]
