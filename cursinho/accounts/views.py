from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings

from cursinho.core.utils import generate_hash_key

from .forms import (UserForm, DetailsUserForm)
# from .models import PasswordReset

User = get_user_model()
@login_required(login_url='accounts:login')
def home(request):
    form = User.objects.filter(is_active=True).exclude(pk=1).order_by('username')
    context = {
        'loading': 'Docentes',
        'form': form,
    }
    template_name = "accounts/home.html"
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def insert(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accounts:home')

    template_name = 'accounts/insert.html'
    context = {
        'loading': 'Docentes',
        'form': form,
    }
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def details(request, slug):
    docente = get_object_or_404(User, slug=slug)

    form = DetailsUserForm(instance=docente or None)
    template_name = 'accounts/details.html'
    context = {
        'loading': 'Docentes',
        'form': form,
    }
    return render(request, template_name, context)
