from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings

from cursinho.core.utils import generate_hash_key

from .forms import UserForm
# from .models import PasswordReset

User = get_user_model()
@login_required(login_url='accounts:login')
def home(request):
    context = {
        'loading': 'Docentes',
    }
    template_name = "accounts/home.html"
    return render(request, template_name, context)

def insert(request):
    # form = RegisterAlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alunos:home')

    context = {
        'loading': 'Docentes',
        # 'form': form,

    }
    template_name = 'accounts/register.html'
    return render(request, template_name, context)
