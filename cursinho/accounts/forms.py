import itertools

from django import forms
from django.utils.text import slugify
from django.utils.timezone import datetime
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
    # '  my_field: forms.MultipleChoiceField(choices=SOME_CHOICES, widget=forms.CheckboxSelectMultiple())
    # 'cargo': forms.Select(attrs={'class': 'select'}, choices=Cargo), # campo de menu selecao

}

class UserForm(forms.ModelForm):
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

        if len(password1)<6 or len(password2)<6:
            raise forms.ValidationError('Senha deve conter no mínimo 6 carateres')
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])

        user.is_superuser = False
        user.is_staff = True

        user.date_joined = datetime.now()

        user.slug = orig = slugify(user.username)

        for x in itertools.count(1):
            if not User.objects.filter(slug=user.slug).exists():
                break
            user.slug = '%s%d' % (orig, x)

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'name', 'cel', 'email',
            'end', 'num_end', 'comp_end', 'cep_end',
            'bairro_end', 'cargo', 'com']

        widgets = Atributos

class DetailsUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'cel', 'email',
            'end', 'num_end', 'comp_end', 'cep_end',
            'bairro_end', 'cargo', 'com']

        widgets = Atributos
