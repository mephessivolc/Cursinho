import itertools

from django import forms
from django.utils.text import slugify

from .models import RegisterAluno

Fields = ['name', 'email', 'sex', 'dCronicas', 'estcivil',
    'qtdfilhos', 'concEnsMed', 'bolsaEnsMed']

Widgets = {
    'name': forms.TextInput(attrs={'placeholder': 'Nome',
        'class': 'form-control',}),
    'email': forms.EmailInput(attrs={'placeholder': 'Email',
        'class': 'form-control',}),
    'sex': forms.TextInput(attrs={'placeholder': 'Sexo',
        'class': 'form-control',}),
    'dCronicas': forms.TextInput(attrs={'placeholder': 'Doenças Crônicas',
        'class': 'form-control',}),
    'estcivil': forms.TextInput(attrs={'placeholder': 'Estado Civil',
        'class': 'form-control',}),
    'qtdfilhos': forms.TextInput(attrs={'placeholder': 'Quantidade de Filhos',
        'class': 'form-control',}),
    'concEnsMed': forms.TextInput(attrs={'placeholder': 'Conclusão do Ensino Médio',
        'class': 'form-control',}),
    'bolsaEnsMed': forms.TextInput(attrs={'placeholder': 'Bolsa no Ensino Médio',
        'class': 'form-control',}),
}

class AlunoForm(forms.ModelForm):

    def save(self, commit=True):
        pupil = super(AlunoForm, self).save(commit=False)
        dbPupil = RegisterAluno.objects

        pupil.slug = orig = slugify(pupil.name)

        for x in itertools.count(1):
            if not dbPupil.filter(slug=pupil.slug).exists():
                break
            pupil.slug = '%s-%d' % (orig, x)

        if commit:
            pupil.save()

        return pupil


    class Meta:
        model = RegisterAluno
        fields = Fields

        widgets = Widgets

class DetailsUserForm(forms.ModelForm):

    class Meta:
        model = RegisterAluno
        fields = Fields

        widgets = Widgets
