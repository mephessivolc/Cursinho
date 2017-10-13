from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .forms import AlunoForm
from .models import RegisterAluno
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
    if form.is_valid():
        form.save()
        return redirect('alunos:home')

    template_name = 'alunos/insert.html'
    context = {
        'loading': 'Alunos',
        'form': form,
    }
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def details(request, slug=None):
    aluno = get_object_or_404(RegisterAluno, slug=slug)

    form = AlunoForm(instance=aluno or None)
    template_name = 'alunos/details.html'
    context = {
        'loading': 'Alunos',
        'form': form,
    }
    return render(request, template_name, context)
