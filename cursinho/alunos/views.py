from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .forms import RegisterAlunoForm
# Create your views here.

@login_required(login_url='accounts:login')
def home(request):

    context = {
        'loading': 'Alunos',
    }
    template_name = "alunos/home.html"
    return render(request, template_name, context)

def insert(request):
    form = RegisterAlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alunos:home')

    context = {
        'loading': 'Alunos',
        'form': form,

    }
    template_name = 'alunos/register.html'
    return render(request, template_name, context)
