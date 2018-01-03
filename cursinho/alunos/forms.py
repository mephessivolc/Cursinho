# import itertools

from django import forms
from django.utils.text import slugify
from django.utils.timezone import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from cursinho.core.mail import send_mail_template
from cursinho.core.utils import (generate_number, random_key)
from cursinho.accounts.forms import UserForm
from cursinho.accounts.models import User

from .models import FamiliaAluno

User = get_user_model()

Atributos = {
    # 'per': forms.Select(attrs={'class':'select'}, choices=SelPer), # campo de menu selecao
    'username': forms.TextInput(attrs={'placeholder': 'Apelido',
        'class': 'form-control'}),
    'name': forms.TextInput(attrs={'placeholder': 'Nome Completo',
        'class': 'form-control'}),
    'end': forms.TextInput(attrs={'placeholder': 'Endereço',
        'class': 'form-control'}),
    'num_end': forms.TextInput(attrs={'placeholder': 'Numero',
        'class': 'form-control'}),
    'comp_end': forms.TextInput(attrs={'placeholder': 'Complemento',
        'class': 'form-control'}),
    'bairro_end': forms.TextInput(attrs={'placeholder': 'Bairro',
        'class': 'form-control'}),
    'cep_end': forms.TextInput(attrs={'placeholder': 'CEP',
        'class': 'form-control'}),
    'cel': forms.TextInput(attrs={'placeholder': '(99) 9.9999-9999',
        'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'placeholder': 'email@pessoal.com',
        'class': 'form-control'}),
}

FamiliaAtributos = {
    'nome': forms.TextInput(attrs={'placeholder': 'Nome',
        'class': 'form-control'}),
    'parente': forms.TextInput(attrs={'placeholder': 'Parentesco',
        'class': 'form-control'}),
    'esc': forms.EmailInput(attrs={'placeholder': 'Escolaridade',
        'class': 'form-control'}),
    'salario': forms.EmailInput(attrs={'placeholder': 'Renda',
            'class': 'form-control'}),
}

class AlunoForm(UserForm):
    # password1 = forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
    password1 = forms.CharField(label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Senha'}))
    password2 = forms.CharField(label=u'Confirmação',
        widget=forms.PasswordInput(attrs={'class': 'form-control padding-right-1',
        'placeholder': 'Confirmação de Senha'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):
        user = super(AlunoForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])

        user.is_superuser = False
        user.is_staff = False

        user.date_joined = datetime.now()

        verify = True
        while verify:
            user.slug = slugify("%s%s"%(datetime.now().year, generate_number()))
            if not User.objects.filter(slug=user.slug).exists():
                verify = False

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'name', 'cel', 'email',
            'end', 'num_end', 'comp_end', 'cep_end',
            'bairro_end', ]

        widgets = Atributos

class DetailsAlunosForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'cel', 'email',
            'end', 'num_end', 'comp_end', 'cep_end',
            'bairro_end',]

        widgets = Atributos

class FamiliaAlunosForm(forms.ModelForm):

    def save(self, commit=True, ref=None):
        familia = super(FamiliaAlunosForm, self).save(commit=False)

        familia.ref_aluno = ref
        # Pensar em adicionar varios registros no banco de dados
        # adicionar no insert.html o javascript e ver se colocar os campos no lugar certo
        # colocar o link da pagina no insert_contact_url do javascript
        # o arquivo do javascript é initial.js
        if commit:
            familia.save()

        return familia

    class Meta:
        model = FamiliaAluno
        fields = ['name', 'parente', 'esc', 'salario']
