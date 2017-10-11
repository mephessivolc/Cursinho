from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from cursinho.core.mail import send_mail_template
from cursinho.core.utils import generate_hash_key

# from .models import PasswordReset

User = get_user_model()

Cargo = (
    ('0', 'Administrativo'),
    ('1', 'Docente'),
    ('2', 'Plantonista'),
    ('3', 'Outro'),
)

Atributos = {
    # 'per': forms.Select(attrs={'class':'select'}, choices=SelPer), # campo de menu selecao
    'username': forms.TextInput(attrs={'placeholder': 'Apelido',
        'class': 'form-control'}),
    'name': forms.TextInput(attrs={'placeholder': 'Nome Completo',
        'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'placeholder': 'email@pessoal.com',
        'class': 'form-control'}),
    'password': forms.TextInput(attrs={'class': 'form-control',
    'type': 'password'}),
    #  my_field: forms.MultipleChoiceField(choices=SOME_CHOICES, widget=forms.CheckboxSelectMultiple())
    'cargo': forms.Select(attrs={'class': 'select'}, choices=Cargo), # campo de menu selecao
}

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = Atributos

class UserForm(forms.ModelForm):

    password1 = forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Senha'})
    password1 = forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Confirmação da Senha'})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password',]

        widgets = Atributos

class DetailsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'email',]

        widgets = Atributos
