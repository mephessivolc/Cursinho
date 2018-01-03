from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from cursinho.accounts.models import User

from .forms import (AlunoForm, DetailsAlunosForm, FamiliaAlunosForm)
# Create your views here.

@login_required(login_url='core:login')
def home(request):

    form = None
    if request.user.is_staff:
        # form = User.objects.filter(is_active=True).filter(is_staff=False).exclude(pk=1).order_by('username')
        form = User.objects.filter(is_active=True).filter(is_staff=False).order_by('username')
        template_name = "alunos/home.html"

    context ={
        'loading': 'Alunos',
        'form': form,
    }

    return render(request, template_name, context)

@login_required(login_url='core:login')
def insert(request):
    form = AlunoForm(request.POST or None)
    formCont = FamiliaAlunosForm(request.POST or None)

    if form.is_valid():
        resp = form.save()

        return redirect('alunos:home')

    template_name = 'alunos/insert.html'
    context = {
        'loading': 'Alunos',
        'form': form,
        'formCont': formCont,
    }

    return render(request, template_name, context)

@login_required(login_url='core:login')
def details(request, slug):
    alunos = get_object_or_404(User, slug=slug)

    form = DetailsAlunosForm(instance=alunos or None)

    template_name = 'alunos/details.html'
    context = {
        'loading': 'Alunos',
        'form': form,
        'cod': alunos.slug,
    }

    return render(request, template_name, context)
