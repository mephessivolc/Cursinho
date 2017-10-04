from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from cursinho.accounts.models import User
from cursinho.accounts.forms import UserForm, DetailsForm

from cursinho.docentes.forms import RegisterUserForm
# Create your views here.

@login_required
def home(request):
    form = User.objects.all().order_by('username')
    context ={
        'loading': 'Docentes',
        'form': form,
    }
    template_name = "docentes/home.html"
    return render(request, template_name, context)

@login_required
def insert(request):
    form = RegisterUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('docentes:home')

    context = {
        'loading': 'Docentes',
        'form': form,
    }
    template_name = "docentes/user.html"
    return render(request, template_name, context)

@login_required
def details(request, slug):
    docente = get_object_or_404(User, slug=slug)

    form = DetailsForm(instance=docente or None)
    template_name = 'docentes/details.html'
    context = {
        'loading': 'Docentes',
        'form': form,
    }
    return render(request, template_name, context)
