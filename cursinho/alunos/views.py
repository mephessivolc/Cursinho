from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .forms import AlunoForm
from .models import RegisterAluno

from cursinho.core.forms import (RegisterEndForm, RegisterContactForm)
from cursinho.core.models import (RegisterEnd, RegisterContact)
# Create your views here.

@login_required(login_url='accounts:login')
def home(request):
    form = RegisterAluno.objects.all()
    context = {
        'loading': 'Alunos',
        'form': form,
    }
    template_name = "alunos/home.html"
    return render(request, template_name, context)

def insert(request):
    form = AlunoForm(request.POST or None)
    formEnd = RegisterEndForm(request.POST or None)
    formContact = RegisterContactForm(request.POST or None)

    if form.is_valid() and formEnd.is_valid() and formContact.is_valid():
        idPupil = form.save()
        formEnd.save(idAluno=idPupil[0])
        formContact.save(idAluno=idPupil[0])

        return redirect('alunos:home')

    template_name = 'alunos/insert.html'
    context = {
        'loading': 'Alunos',
        'form': form,
        'formEnd': formEnd,
        'formContact': formContact,
    }
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def details(request, slug=None):
    aluno = get_object_or_404(RegisterAluno, slug=slug)
    end = get_object_or_404(RegisterEnd, idPupil=aluno.id)
    contact = get_object_or_404(RegisterContact, idPupil=aluno.id)

    form = AlunoForm(request.POST or None, instance=aluno)
    formEnd = RegisterEndForm(request.POST or None, instance=end)
    formContact = RegisterContactForm(request.POST or None, instance=contact)

    template_name = 'alunos/details.html'
    context = {
        'loading': 'Alunos',
        'form': form,
        'formEnd': formEnd,
        'formContact': formContact,
    }
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def update(request, slug=None):
    aluno = get_object_or_404(RegisterAluno, slug=slug)
    end = get_object_or_404(RegisterEnd, idPupil=aluno.id)
    contact = get_object_or_404(RegisterContact, idPupil=aluno.id)

    form = AlunoForm(request.POST or None, instance=aluno)
    formEnd = RegisterEndForm(request.POST or None, instance=end)
    formContact = RegisterContactForm(request.POST or None, instance=contact)

    if form.is_valid() and formEnd.is_valid():
        resp = form.save()
        formEnd.save()
        formContact.save()

        return redirect('alunos:details', resp[1])

    template_name = 'alunos/update.html'
    context = {
        'loading': 'Alunos',
        'form': form,
        'formEnd': formEnd,
        'formContact': formContact,
    }
    return render(request, template_name, context)
