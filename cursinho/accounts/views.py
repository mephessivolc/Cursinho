from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings

from cursinho.core.utils import generate_hash_key
from cursinho.core.forms import RegisterEndForm

from .forms import (UserForm, DetailsUserForm)
# from .models import PasswordReset

User = get_user_model()
@login_required(login_url='core:login')
def home(request):
    form = User.objects.filter(is_active=True).filter(is_staff=True).exclude(pk=1).order_by('name')
    context = {
        'loading': 'Docentes',
        'form': form,
    }
    template_name = "accounts/home.html"
    return render(request, template_name, context)

@login_required(login_url='core:login')
def insert(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        resp = form.save()
        return redirect('accounts:home')

    template_name = 'accounts/insert.html'
    context = {
        'loading': 'Docentes',
        'form': form,
    }

    return render(request, template_name, context)

@login_required(login_url='core:login')
def details(request, slug):
    docente = get_object_or_404(User, slug=slug)

    form = DetailsUserForm(instance=docente or None)

    if docente.cargo == 'Prof':
        cargo = "Professor"
    elif docente.cargo == 'Plan':
        cargo = 'Plantonista'
    elif docente.cargo == 'Cul':
        cargo = 'Cultural'
    else:
        cargo = 'Nenhum'

    if docente.com == 'Adm':
        com = 'Administração'
    elif docente.com == 'Ped':
        com = 'Pedagógica'
    elif docente.com == 'Cul':
        com = 'Cultural'
    else:
        com = 'Nenhum'

    template_name = 'accounts/details.html'
    context = {
        'loading': 'Docentes',
        'form': form,
        'cargo': cargo,
        'com': com,
    }

    return render(request, template_name, context)
